from notebook import notebookapp
import urllib, json, os, ipykernel, ntpath

FILE_ERROR = "Can't identify the notebook {}."
CONN_ERROR = "Unable to access server;\n \
            + ipynbname requires either no security or token based security."

def _get_kernel_id():
    """ Returns the kernel ID of the ipykernel.
    """
    connection_file = os.path.basename(ipykernel.get_connection_file())
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]
    return kernel_id


def _get_sessions(srv):
    """ Given a server, returns sessions, or HTTPError if access is denied.
        NOTE: Works only when either there is no security or there is token
        based security. An HTTPError is raised if unable to connect to a 
        server.
    """
    try:
        qry_str = ""
        token = srv['token']
        if token:
            qry_str = f"?token={token}"
        url = f"{srv['url']}api/sessions{qry_str}"
        req = urllib.request.urlopen(url)
        return json.load(req)
    except:
        raise urllib.error.HTTPError(CONN_ERROR)


def _get_nb_path(sess, kernel_id):
    """ Given a session and kernel ID, returns the notebook path for the
        session, or None if there is no notebook for the session.    
    """
    if sess['kernel']['id'] == kernel_id:
        return sess['notebook']['path']
    return None


def name():
    """ Returns the short name of the notebook w/o the .ipynb extension,
        or raises a FileNotFoundError exception if it cannot be determined.     
    """
    kernel_id = _get_kernel_id()
    for srv in notebookapp.list_running_servers():
        try:
            sessions = _get_sessions(srv)
            for sess in sessions:
                nb_path = _get_nb_path(sess, kernel_id)
                if nb_path:
                    return ntpath.basename(nb_path).replace('.ipynb', '')
        except:
            pass  # There may be stale entries in the runtime directory
    raise FileNotFoundError(FILE_ERROR.format('name'))


def path():
    """ Returns the absolute path of the notebook,
        or raises a FileNotFoundError exception if it cannot be determined.
    """
    kernel_id = _get_kernel_id()
    for srv in notebookapp.list_running_servers():
        try:
            sessions = _get_sessions(srv)
            for sess in sessions:
                nb_path = _get_nb_path(sess, kernel_id)
                if nb_path:
                    return os.path.join(srv['notebook_dir'], nb_path)
        except:
            pass  # There may be stale entries in the runtime directory
    raise FileNotFoundError(FILE_ERROR.format('path'))

