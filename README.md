
![Image](https://github.com/user-attachments/assets/8fe9a2be-1fed-4af6-9250-c91bc1502706)

# gerador_legendas
Open Source python script + tools needed to automate subtitles in videos


<br>

## Guia (terminal):

1. Ter instalado localmente:
    > Python
    - python --version
    - winget seach python
    - winget install Python.Python.3.14.3
    - python --version
    - python -m pip install --upgrade pip
  
   <br>

    > Whisper AI
    - python -m pip show openai-whisper
    - python -m pip install --upgrade pip
    - python -m pip install openai-whisper
    - python -m pip show openai-whisper

    <br>

    > FFmpeg
    - ffmpeg -version
    - https://www.gyan.dev/ffmpeg/builds/
    - download: ffmpeg-2026-02-04-git-627da1111c-full_build
    - extrair pasta > definir caminho "bin" como variável de ambiente "Path"
    - ffmpeg -version
  
    <br>

    > Torch (opcional, usa GPU em vez da CPU, acelera muito o processo)

<br>

2. Download do script "__legendador.py__"
    > script > legendador.py


## Utilização:

1. Deixar o script e o video na mesma localização
    > ⚠️ O caminho absoluto para a pasta e do ficheiro não deve conter caracteres especiais.

<br>

2. Abrir o terminal e navegar até a localização dos dois ficheiros

<br>

3. Usar o comando: <br>
   ***python legendador.py <nome_video.extensao>***
    <br>
    
    ou
    <br>
    
    ***python legendador.py <nome_video.extensao> <2>***
   
    <br>
       ⚠️ O <2> indica quantas palavras querem por timestamp 

<br>

## Adicional
1. Se tiver dificuldades fale comigo pelo:
    - [instagram](https://www.instagram.com/laercio.dev/)
    - [Linkedin](https://www.linkedin.com/in/laerciosantosdev/)

## Upcoming Enhancements
1. Second progress bar a indicar o estado da conversão do áudio para texto


### gerador_legendas 2026 by *Laércio Santos* 
