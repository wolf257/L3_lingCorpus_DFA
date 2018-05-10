#!/usr/bin/env python3

def POS_finder_fr(pos_from_treetagger, lemme):
    pos = 'classe_inconnue'

    if (lemme == "que") :
        pos = "que+"
    elif (lemme == "le") or (lemme == "la") or (lemme == "les") :
        pos = 'le+' 
    elif (lemme == "de") or (lemme == 'du') or (lemme == 'des') :
        pos = 'de+' 

    else :
    
        if "VER" in pos_from_treetagger :
            if ("être" in lemme) :
                pos = 'verbe_etre' 
            
            elif ("valoir" in lemme) or ("diminuer" in lemme) or ("augmenter" in lemme) \
            or ("doubler" in lemme) or ("tripler" in lemme) or ("quadrupler" in lemme) :
                pos = 'verbe_comp' 
            else :
                pos = 'verbe'
            
        if "ADJ" in pos_from_treetagger :
            pos = 'adjectif'
        
        if "ADV" in pos_from_treetagger :
            if (lemme == "plus") or (lemme == "moins") or (lemme == "aussi") or (lemme == 'autant'):
                pos = 'adverbe_comp' 
            else :
                pos = 'adverbe'

        if "DET" in pos_from_treetagger :
            pos = 'determinant'
    
        if "PRO" in pos_from_treetagger :
            pos = 'pronom'

        if ("NOM" in pos_from_treetagger) or ("NAM" in pos_from_treetagger) :
            pos = 'nom'
        if "NUM" in pos_from_treetagger :
            pos = 'nombre'

        if "PRP" in pos_from_treetagger :
            pos = 'preposition'
        
        if "PUN" in pos_from_treetagger :
            pos = 'ponctuation'
        
        if "KON" in pos_from_treetagger :
            pos = 'conjonction'
                
        if "SENT" in pos_from_treetagger :
            pos = 'ponctuation'

    return str(pos)

def POS_finder_en(pos_from_treetagger, lemme):
    pos = 'classe_inconnue'

    if (lemme == "que") :
        pos = "que+"
    elif (lemme == "le") or (lemme == "la") or (lemme == "les") :
        pos = 'le+' 
    elif (lemme == "de") or (lemme == 'du') or (lemme == 'des') :
        pos = 'de+' 

    else :
    
        if "VER" in pos_from_treetagger :
            if ("être" in lemme) :
                pos = 'verbe_etre' 
            
            elif ("valoir" in lemme) or ("diminuer" in lemme) or ("augmenter" in lemme) \
            or ("doubler" in lemme) or ("tripler" in lemme) or ("quadrupler" in lemme) :
                pos = 'verbe_comp' 
            else :
                pos = 'verbe'
            
        if "ADJ" in pos_from_treetagger :
            pos = 'adjectif'
        
        if "ADV" in pos_from_treetagger :
            if (lemme == "plus") or (lemme == "moins") or (lemme == "aussi") or (lemme == 'autant'):
                pos = 'adverbe_comp' 
            else :
                pos = 'adverbe'

        if "DET" in pos_from_treetagger :
            pos = 'determinant'
    
        if "PRO" in pos_from_treetagger :
            pos = 'pronom'

        if ("NOM" in pos_from_treetagger) or ("NAM" in pos_from_treetagger) :
            pos = 'nom'
        if "NUM" in pos_from_treetagger :
            pos = 'nombre'

        if "PRP" in pos_from_treetagger :
            pos = 'preposition'
        
        if "PUN" in pos_from_treetagger :
            pos = 'ponctuation'
        
        if "KON" in pos_from_treetagger :
        # if ("que" in lemme) :
        #     pos = "que+"
            pos = 'conjonction'
                
        if "SENT" in pos_from_treetagger :
            pos = 'ponctuation'

    return str(pos)
