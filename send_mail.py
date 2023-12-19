import subprocess
import configparser

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['Config']

def main():

    config_params = read_config_file('config.config')

    # Obtén los valores de los parámetros
    script = config_params.get('script')
    from_address = config_params.get('from_address')
    to_address = config_params.get('to_address')
    server_port = config_params.get('server_port')
    api_username = config_params.get('api_username')
    api_token = config_params.get('api_token')
    subject = config_params.get('subject')
    message = config_params.get('message')
    disable_tls = config_params.get('disable_tls')

    def read_html_file(file_path):
        with open(file_path, 'r') as file:
            html_content = file.read()
        return html_content

    file_path = message
    file_content = read_html_file(file_path)

    if disable_tls == "yes":
        command = f'{script} -f {from_address} -t {to_address} -s {server_port} -xu {api_username} -xp {api_token} -u "{subject}" -m "{file_content}" -o tls=no'
    elif disable_tls == "no":
        command = f'{script} -f {from_address} -t {to_address} -s {server_port} -xu {api_username} -xp {api_token} -u "{subject}" -m "{file_content}" -o tls=yes'
    elif disable_tls == "auto":
        command = f'{script} -f {from_address} -t {to_address} -s {server_port} -xu {api_username} -xp {api_token} -u "{subject}" -m "{file_content}" -o tls=auto'
    else:
        print('Specify Tls usage at config file.')
        return

    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
