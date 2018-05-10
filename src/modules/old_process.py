#!/usr/bin/env python3
#-*- coding : utf-8 -*-

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     PRESENTATION DU MODULE :
#          Ce modules rassemble les fonctions de fonctions
#          Dans le souci de ne pas surcharger le fichier main.py
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

########################################################
# LIST FUNCTIONS IN MODULES
#
#     + tour_du_corpus()
#     + tour_des_fichiers()
#     + generation_dico_corpus_pr_xml()
#     + creer_et_remplir_fichier_synthese_xml()
#     + creer_et_remplir_fichier_dtd()
#     + generation_et_execution_script_bash_validation_dtd()
#
########################################################

import os
import re
import random
import codecs
import subprocess

from collections import defaultdict

import pprint , io

import modules.others as others
import modules.ponctuation_texte as ponctuation_texte
import modules.statistiques as statistiques
import modules.writing_in_files as writing_in_files
import modules.tagging as tagging

# Lien vers les dossiers de la racine ############################################
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from settings import PROJECT_ROOT, CORPUS_PHRASES, CORPUS_TEXTES, MORPHALOU_ROOT, TREETAGGER_ROOT
###################################################################################

dossier_morphalou = MORPHALOU_ROOT

##############################################################
# Fonction : tour_du_corpus
# Input :
##############################################################
def tour_du_corpus(path_to_corpus):
    ''' Creer et remplit le fichier 0_stats_du_corpus et 1_distribution_mot_du_corpus '''

    # VAR
    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))

    print('++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous travaillons sur le corpus : {}'.format(nom_corpus))

    #CREATION DOSSIER STATISTIQUES a la RACINE DU CORPUS
    others.creation_folder(path_to_corpus, 'statistiques')

    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'
    #VAR
    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nom_fichier_distribution_corpus = path_to_corpus_stat_folder + '1_distribution_de_' + nom_corpus + '.txt'

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    dico_distribution_mots_corpus = {}
    ts_text_in_one_string = []

    nb_mots_corpus = 0
    nb_phrases = 0

    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        nb_mots_corpus += len(liste_exploitable_txt)

        for word in liste_exploitable_txt :
            if word == '.' or word == '?' or word == '!' :
                nb_phrases += 1

        ts_text_in_one_string += liste_exploitable_txt

    distribution_mots_corpus = statistiques.wordsDistributionUpdate_dict_from_list(dico_distribution_mots_corpus, ts_text_in_one_string)

    writing_in_files.remplissage_stat_corpus(nom_fichier_stats_corpus, nom_corpus, files_in_corpus, nb_mots_corpus, nb_phrases)

    writing_in_files.ecrire_distribution_mot_corpus(nom_fichier_distribution_corpus, path_to_corpus, distribution_mots_corpus)

##############################################################
# Fonction : tour_des_fichiers()
# Input :
##############################################################
def tour_des_fichiers(path_to_corpus):
    ''' Creer et remplit le fichier 0_stats et 1_distribution_mot pour chaque fichier du corpus '''

    #VAR
    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'

    for file in files_in_corpus :
        #VAR
        path_file = os.path.join(path_to_corpus, file)

        ###################################
        #CREATION LISTE À EXPLOITER
        liste_exploitable_txt = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_word_distribution(path_file)
        ###################################

        nb_mots_texte = len(liste_exploitable_txt)
        nb_phrases = 0

        for word in liste_exploitable_txt :
            if word == '.' or word == '?' or word == '!' :
                nb_phrases += 1

        distribution_mots_txt = statistiques.wordsDistribution_dict_from_list(liste_exploitable_txt)

        writing_in_files.remplissage_stat_texte(file, path_to_corpus, path_to_corpus_stat_folder, nb_mots_texte, nb_phrases)

        writing_in_files.ecrire_distribution_mot_texte(file, path_to_corpus, path_to_corpus_stat_folder, distribution_mots_txt)

    print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')

##############################################################
# Fonction : generation_corpus_xml()
# Input :
##############################################################

def generation_corpus_xml(path_to_corpus, version='light'):
    #VAR
    dico_tag_corpus = defaultdict(lambda: defaultdict(dict))
    file_morphalou = others.load_morphalou(dossier_morphalou)

    nom_corpus = os.path.basename(os.path.normpath(path_to_corpus))

    if nom_corpus == 'corpus_professeur' :
        num_corpus = 1
    else :
        num_corpus = 2

    #VAR
    reference_corpus = 'c'+str(num_corpus)

    print('\n++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n++ Nous allons tagger et recupérer les mots du corpus {}. \n Souhaitez-nous bonne chance'.format(nom_corpus))

    #CREATION DOSSIER XML a la RACINE DU CORPUS
    others.creation_folder(path_to_corpus, 'xml')

    #VAR
    path_to_corpus_stat_folder = path_to_corpus+'statistiques/'

    path_to_corpus_xml_folder = path_to_corpus+'xml/'
    nom_fichier_xml_corpus = path_to_corpus_xml_folder + 'rendu_de_' + nom_corpus + '.xml'

    #XML : balise <corpus type_corpus='valeur'>
    writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'corpus', 1, 'type_corpus', nom_corpus)

    files_in_corpus = None
    files_in_corpus = others.list_text_in_folder_as_list(path_to_corpus)

    nom_fichier_distribution_corpus ='1_distribution_de_' + nom_corpus + '.txt'
    path_fichier_distribution_corpus = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_corpus )
    liste_fichier_distribution_corpus = others.import_distribution_as_list(path_fichier_distribution_corpus)

    nom_fichier_stats_corpus = path_to_corpus_stat_folder + '0_stats_de_' + nom_corpus + '.txt'
    nb_mots_corpus, nb_phrases_corpus, nb_moyen_mots_par_phrase_corpus = others.recherche_stats_base_texte(nom_fichier_stats_corpus)

    #######
    # Niveau des textes
    ######

    text_for_tagg = []

    for file in files_in_corpus:
        path_file = os.path.join(path_to_corpus, file)

        nom_fichier_distribution_texte = file[:-4] + '_2_distributions.txt'
        path_fichier_distribution_texte = os.path.join(path_to_corpus_stat_folder, nom_fichier_distribution_texte)
        liste_fichier_distribution_texte = others.import_distribution_as_list(path_fichier_distribution_texte)

        nom_fichier_stats_texte = path_to_corpus_stat_folder+file[:-4]+'_1_stats.txt'
        nb_mots_texte, nb_phrases_texte, nb_moyen_mots_par_phrase_texte = others.recherche_stats_base_texte(nom_fichier_stats_texte)
        #print('TEST : {}, {}, {}'.format(nb_mots_texte, nb_phrases_texte, nb_moyen_mots_par_phrase_texte))

        num_texte = int(files_in_corpus.index(file))
        reference_texte = 'c'+str(num_corpus)+'t'+str(num_texte)

        #XML : balise <text text_id=CxTx>
        writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'text', 2, 'text_id', reference_texte)

        ###################################
        #CREATION LISTE À EXPLOITER
        text_for_tagg = ponctuation_texte.du_texte_a_sa_liste_exploitable_par_tagging(path_file)
        ###################################

        compteur_ligne = 0
        nb_lignes_in_texte = len(text_for_tagg)
        nb_lignes_a_traiter = 1

        if version == 'complet' :
            nb_lignes_a_traiter = nb_lignes_in_texte
        else :
            nb_lignes_a_traiter = 10

        if nb_lignes_a_traiter > nb_lignes_in_texte :
            nb_lignes_a_traiter = nb_lignes_in_texte

        while compteur_ligne < nb_lignes_a_traiter :
            num_line = compteur_ligne
            line = text_for_tagg[compteur_ligne]

            reference_line = 'c'+str(num_corpus)+'t'+str(num_texte)+'s'+str(num_line)

            #XML : balise <sentence sentence_id=CxTxSx>
            writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_corpus, 'sentence', 3, 'sentence_id', reference_line)

            print('\n\n{}'.format('='*35))
            print('***Ref ligne : {}'.format(reference_line))
            print('***Contenu : {}'.format(line))

            tagging.tagger_phrase_et_ajouter_au_texte_ref_to_word(line, nom_fichier_xml_corpus, liste_fichier_distribution_corpus, liste_fichier_distribution_texte, file_morphalou, num_corpus, num_texte, num_line, nb_mots_corpus, nb_mots_texte)

            writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'sentence', 3)

            compteur_ligne +=1

        writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'text', 2)

    writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_corpus, 'corpus', 1)

##############################################################
# Fonction : creer_et_remplir_fichier_synthese_xml()
##############################################################
def creer_et_remplir_fichier_synthese_xml(root_project, liste_corpus) :
    others.creation_folder(root_project+'/', 'resultats_xml')
    path_to_project_synthese_xml_folder = root_project+'/resultats_xml/'
    nom_fichier_xml_synthese = path_to_project_synthese_xml_folder + 'synthese_xml_total.xml'

    print('\t\tRemplissage du fichier synthese_xml_total.')

    with codecs.open(nom_fichier_xml_synthese, mode='w', encoding='utf8') as file :
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>')
        file.write('\n<!DOCTYPE banque_donnees SYSTEM "synthese_xml_total.dtd">')

    writing_in_files.ecrire_xml_balise_ouvrante(nom_fichier_xml_synthese, 'banque_donnees', 0)

    for corpus in liste_corpus :
        nom_corpus = os.path.basename(os.path.normpath(corpus))
        path_to_corpus_xml_folder = corpus+'xml/'
        nom_fichier_xml_corpus = path_to_corpus_xml_folder + 'rendu_de_' + nom_corpus + '.xml'

        with codecs.open(nom_fichier_xml_synthese, mode='a', encoding='utf8') as file_out :
            with codecs.open(nom_fichier_xml_corpus, mode='r', encoding='utf8') as file_in :
                for line in file_in :
                    file_out.write('{}'.format(line))


    writing_in_files.ecrire_xml_balise_fermante(nom_fichier_xml_synthese, 'banque_donnees', 0)

    print('\t\t\tFin du remplissage du fichier synthese_xml_total.')

##############################################################
# Fonction : creer_et_remplir_fichier_synthese_xml()
##############################################################
def creer_et_remplir_fichier_dtd(root_project) :
    path_to_project_synthese_xml_folder = root_project+'/resultats_xml/'

    if not path_to_project_synthese_xml_folder :
        others.creation_folder(root_project+'/', 'resultats_xml')

    nom_fichier_dtd = path_to_project_synthese_xml_folder + 'synthese_xml_total.dtd'

    print('\t\tCreation de la dtd.')
    try :
        with codecs.open(nom_fichier_dtd, mode='w', encoding='utf8') as file :
            file.write('<!ELEMENT banque_donnees (corpus+)>')

            file.write('\n\n<!ELEMENT corpus (text+)>')
            file.write('\n<!ATTLIST corpus type_corpus (corpus_professeur|corpus_litterature) #REQUIRED>')

            file.write('\n\n<!ELEMENT text (sentence+)>')
            file.write('\n<!ATTLIST text text_id ID #REQUIRED>')

            file.write('\n\n<!ELEMENT sentence (word+)>')
            file.write('\n<!ATTLIST sentence sentence_id ID #REQUIRED>')

            file.write('\n\n<!ELEMENT word (morphology, statistics)+>')
            file.write('\n<!ATTLIST word word_id ID #REQUIRED>')
            file.write('\n<!ATTLIST word word_form CDATA #REQUIRED>')

            file.write('\n\n<!ELEMENT morphology (lemme, POS_treetagger, POS_morphalou?, genre?, nombre?)>')
            file.write('\n<!ELEMENT lemme (#PCDATA)>')
            file.write('\n<!ELEMENT POS_treetagger (#PCDATA)>')
            file.write('\n<!ELEMENT POS_morphalou (#PCDATA)>')
            file.write('\n<!ELEMENT genre (#PCDATA)>')
            file.write('\n<!ELEMENT nombre (#PCDATA)>')

            file.write('\n\n<!ELEMENT statistics (nb_apparition_text, nb_apparition_corpus, frequence_in_text, frequence_in_corpus)>')
            file.write('\n<!ELEMENT nb_apparition_text (#PCDATA)>')
            file.write('\n<!ELEMENT nb_apparition_corpus (#PCDATA)>')
            file.write('\n<!ELEMENT frequence_in_text (#PCDATA)>')
            file.write('\n<!ELEMENT frequence_in_corpus (#PCDATA)>')
    except :
        print('\t\t\tLe remplissage a échoué.')
    else :
        print('\t\t\tLa création de la dtd a réussi.')

##############################################################
# Fonction : generation_et_execution_script_bash_validation_dtd()
##############################################################
def generation_et_execution_script_bash_validation_dtd(root_project) :
    path_to_project_synthese_xml_folder = root_project+'/resultats_xml/'

    if not path_to_project_synthese_xml_folder :
        others.creation_folder(root_project+'/', 'resultats_xml')

    nom_script = path_to_project_synthese_xml_folder + 'script_validation_dtd.bash'

    try :
        with codecs.open(nom_script, mode='w', encoding='utf8') as file :
            file.write('#!/bin/bash')
            file.write('\n\nxmllint -noout -dtdvalid synthese_xml_total.dtd synthese_xml_total.xml')
    except :
        print('\\t\tCreation du script bash : echec.')
    else :
        print('\n\t\tLa creation du script bash pour validation de la dtd a reussi.')
        try :
            os.system("chmod +x " + nom_script)
        except:
            print('\t\t\tProbleme pour rendre le script executable.')
        else :
            print('\t\t\tLe script est executable grace à chmod +x.')

            print('\t\t\t\tLancement du script : synthese_xml_total.dtd .' )
            result = str(subprocess.call(nom_script, shell=True, cwd=path_to_project_synthese_xml_folder))

            if result == '' or result == '0' :
                print('\t\t\t\tLa dtd a validé le document grace à xmllint.')
            else :
                print('\t\t\t\tProbleme de validation du document xml.')
