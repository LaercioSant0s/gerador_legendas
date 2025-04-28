import os
import sys
import subprocess
import whisper
import torch


def format_time(seconds: float) -> str:
    """Converts seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hrs:02d}:{mins:02d}:{secs:06.3f}".replace('.', ',')


def process_video(input_path: str, max_words: int = 3) -> None:
    """
    Extrai o áudio do vídeo, transcreve com Whisper e gera um arquivo SRT.

    Args:
        input_path: Caminho para o arquivo de vídeo.
        max_words: Número máximo de palavras por legenda.
    """
    if not os.path.isfile(input_path):
        print(f"Erro: arquivo não encontrado: {input_path}")
        return

    # Extrai áudio em WAV mono 16kHz
    temp_audio = "_temp_audio.wav"
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", temp_audio
    ], check=True)

    # Carrega modelo Whisper
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("large", device=device)
    result = model.transcribe(temp_audio, language="pt", word_timestamps=True)

    # Monta lista de todas as palavras
    words = [w for segment in result["segments"] for w in segment["words"]]

    srt_file = os.path.splitext(os.path.basename(input_path))[0] + ".srt"
    with open(srt_file, "w", encoding="utf-8") as f:
        segment_idx = 1
        buffer = []

        for word in words:
            buffer.append(word)
            if len(buffer) >= max_words:
                start = buffer[0]["start"]
                end = buffer[-1]["end"]
                text = " ".join(w.get("text", w.get("word", "")) for w in buffer)
                text = text.replace("  ", " ")  # Remove espaços duplos

                f.write(f"{segment_idx}\n")
                f.write(f"{format_time(start)} --> {format_time(end)}\n")
                f.write(f"{text}\n\n")

                segment_idx += 1
                buffer.clear()

        # Legendas remanescentes
        if buffer:
            start = buffer[0]["start"]
            end = buffer[-1]["end"]
            text = " ".join(w.get("text", w.get("word", "")) for w in buffer)
            text = text.replace("  ", " ")  # Remove espaços duplos

            f.write(f"{segment_idx}\n")
            f.write(f"{format_time(start)} --> {format_time(end)}\n")
            f.write(f"{text}\n\n")

    # Remove áudio temporário
    os.remove(temp_audio)
    print(f"SRT salvo em: {srt_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py arquivo_video [max_palavras]")
        sys.exit(1)

    video_path = sys.argv[1]
    max_w = int(sys.argv[2]) if len(sys.argv) >= 3 else 3
    process_video(video_path, max_w)
