from notebook import notebookapp
import urllib, json, os, ipykernel, ntpath

def what(path=False):
    """ Returns the short name of the notebook w/o .ipynb
        or get a FileNotFoundError exception if it cannot be determined
        NOTE: works only when the security is token-based or there is also no password
    """
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]

    for srv in notebookapp.list_running_servers():
        try:
            if srv['token']=='' and not srv['password']:
                req = urllib.request.urlopen(srv['url']+'api/sessions')
            else:
                req = urllib.request.urlopen(srv['url']+'api/sessions?token='+srv['token'])
            sessions = json.load(req)
            for sess in sessions:
                if  sess['kernel']['id'] == kernel_id:
                    if path:
                        return os.path.join(srv['notebook_dir'],sess['notebook']['path'])
                    else:
                        nb_path = sess['notebook']['path']
                    return ntpath.basename(nb_path).replace('.ipynb', '')
        except:
            pass  # There may be stale entries in the runtime directory
    raise FileNotFoundError("Can't identify the notebook name")
