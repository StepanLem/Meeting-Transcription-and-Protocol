

1. https://github.com/openai/whisper/discussions/1463
    - делать всё по гайду выше (Онлайн-установка). В частности советы:
    - скачать последнюю версию питон 3.10 с установщиком(обновления безопасности мы не устанавливали, но мб стоит с этим разобраться, когда пойдём в релиз):
            https://www.python.org/downloads/release/python-31011/
    - venv. Перед тем, как pip install whisper, сначала не забыть создать у себя и активировать виртуальное окружение.

2. В этой папке запустить Check_CUDA.py и если выдаёт false, то install torch with CUDA: https://github.com/mmguero/monkeyplug/issues/4:
    - удаляем torch:    python -m pip uninstall torch
    - устанавливаем torch с CUDA:   https://pytorch.org/get-started/locally/