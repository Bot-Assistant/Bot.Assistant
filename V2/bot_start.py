from V2.services import service_dependencies, service_console_messages


def initialization():
    service_console_messages.logo()
    service_dependencies.install_bot_dependencies()


initialization()
