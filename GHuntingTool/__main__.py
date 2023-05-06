import click
from GHuntingTool.Tools.DNSBLDetails import *
from GHuntingTool.Tools.EmailDetails import *
from GHuntingTool.Tools.WhoisLookup import *
@click.group(invoke_without_command=True)
@click.pass_context
def GHuntingTool(ctx):
    '''
\b
  ▄████  ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓ ██▓ ███▄    █   ▄████ ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
 ██▒ ▀█▒▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒██░▄▄▄░▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░▓█  ██▓░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░▒▓███▀▒░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
 ░▒   ▒  ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ░   ░  ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ▒ ░░ ░░   ░ ▒░  ░   ░     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░ ░   ░  ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░       ▒ ░   ░   ░ ░ ░ ░   ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░  ░  ░  ░   ░              ░           ░           ░       ░              ░ ░      ░ ░      ░  ░
                                                                                           
    '''

@GHuntingTool.command()
def WhoisLookup():
    '''
This command help you to find the whois details of domain or IP
    '''

@GHuntingTool.command()
def EmailDetails():
    '''
This command help you get details of email like it's existence, SPF record, DMARC record and other details.
    '''
@GHuntingTool.command()
def DNSBLDetails():
    '''
This command help you get DNSBL details of domain or IP address across multiple DNSBL repos.
    '''

if __name__ == '__main__':
    GHuntingTool()