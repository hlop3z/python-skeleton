import subprocess, argparse, json

with open('config.json') as f:
  CONFIG = json.load(f)

cmd = lambda x: subprocess.run(x, check=True, shell=True)


def setup_origin( path=f"""{ CONFIG['org'] }/{ CONFIG['project'] }""" ):
        cmd(f'git remote add origin git@github.com:{ path }.git')


def update( message=None ):
    if not message: message = "update the repository"
    cmd("git add .")
    cmd(f"""git commit -m '{ message }'""")
    cmd("git push -u origin master")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', nargs="?"         , help='Update Git & Github')
    parser.add_argument('-s', '--setup', action='store_true', help='Setup Github path org/repo')
    args = parser.parse_args()
    if args.setup:
        setup_origin()
    elif args.update:
        update( args.update[0] )
    else:
        update()
