#!/usr/bin/env python3

import pprint , io , os
import codecs

# Lien vers les dossiers de la racine ############################################
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.sys.path.insert(0, parentdir)
# from settings import PROJECT_ROOT, CORPUS_PHRASES, TREETAGGER_ROOT
###################################################################################


##############################################################
# Fonction : creation_folder
##############################################################
def creation_folder(path_to_parent, name_folder):
    print('\n+++ Dossier : ' , name_folder)
    try :
        if not os.path.exists(path_to_parent + name_folder + '/') :
            print('\n\t+++ Création du dossier : ' , name_folder)
            os.makedirs(path_to_parent + name_folder + '/')
        else :
            print('\n\t+++ Dossier déjà existant')

    except :
        print('\tPROBLEME LORS DE LA CREATION DU DOSSIER.')
    else :
        print('\tCréation du dossier réussi.')

if __name__ == '__main__':
    pass
