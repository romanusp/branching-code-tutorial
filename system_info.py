import platform

def kernal_info():
    '''
    Return linux kernal information
    '''
    kernel_info = platform.uname()
    return {'release': kernal_info.release, 'version': kernal_info.version}