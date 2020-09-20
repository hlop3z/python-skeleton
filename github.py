import subprocess, argparse, json, pathlib

PROJECT = pathlib.Path(__file__).resolve().parents[0]

with open('CONFIG.json') as f:
    CONFIG = json.load(f)


cmd = lambda x: subprocess.run(x, check=True, shell=True)



def setup_origin( path=f"""{ CONFIG['org'] }/{ PROJECT.name }""" ):
        cmd(f'git remote add origin git@github.com:{ path }.git')

def setup_update( path=f"""{ CONFIG['org'] }/{ PROJECT.name }""" ):
        cmd(f'git remote set-url origin git@github.com:{ path }.git')

def update( message=None ):
    if not message: message = "update the repository"
    try:
        cmd("git add .")
        cmd(f"""git commit -m '{ message }'""")
        cmd("git push -u origin master")
    except Exception as e:
        print('No updates found')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', nargs="?"         , help='Update Git & Github')
    parser.add_argument('-s', '--setup', action='store_true', help='Setup Github path org/repo')
    parser.add_argument('-su', '--setup_update', action='store_true', help='Setup-Update Github path org/repo')
    args = parser.parse_args()

    if args.setup           : setup_origin()
    elif args.setup_update  : setup_update()
    elif args.update        : update( args.update[0] )
    else                    : update()

if __name__ == '__main__':
    main()
