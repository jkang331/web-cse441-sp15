import invoke


@invoke.task
def build():
    invoke.run('jekyll build -t --config _config.yml,_config-dev.yml')


@invoke.task
def serve():
    invoke.run('jekyll serve -t --config _config.yml,_config-dev.yml --watch --force_polling')
