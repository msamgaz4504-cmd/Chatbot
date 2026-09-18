import hmac
import os

from nltk.chat.util import Chat
import streamlit as st


st.set_page_config(
    page_title="Assistant ENIAC",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# À remplacer lorsque le bureau confirme officiellement la date.
CLUB_CREATION_DATE = "2021"

# Identifiants de démonstration. En production, définissez plutôt les variables
# ENIAC_USERNAME et ENIAC_PASSWORD dans votre environnement.
APP_USERNAME = os.getenv("ENIAC_USERNAME", "eniac")
APP_PASSWORD = os.getenv("ENIAC_PASSWORD", "Eniac@2026")

# ============================================================
# REFLECTIONS FRANÇAISES
# ============================================================

reflections_eniac = {
    "je voudrais": "vous voudriez",
    "j'aimerais": "vous aimeriez",
    "je souhaite": "vous souhaitez",
    "je veux": "vous voulez",
    "je cherche": "vous cherchez",
    "je pense": "vous pensez",
    "je crois": "vous croyez",
    "je peux": "vous pouvez",
    "je dois": "vous devez",
    "je vais": "vous allez",
    "je suis": "vous êtes",
    "j'étais": "vous étiez",
    "j'ai": "vous avez",
    "j'avais": "vous aviez",
    "j'aime": "vous aimez",
    "je participe": "vous participez",
    "je propose": "vous proposez",
    "je connais": "vous connaissez",
    "je comprends": "vous comprenez",
    "je": "vous",

    "vous voudriez": "je voudrais",
    "vous souhaitez": "je souhaite",
    "vous voulez": "je veux",
    "vous cherchez": "je cherche",
    "vous pensez": "je pense",
    "vous croyez": "je crois",
    "vous pouvez": "je peux",
    "vous devez": "je dois",
    "vous allez": "je vais",
    "vous êtes": "je suis",
    "vous étiez": "j'étais",
    "vous avez": "j'ai",
    "vous aviez": "j'avais",
    "vous aimez": "j'aime",
    "vous participez": "je participe",
    "vous proposez": "je propose",
    "vous connaissez": "je connais",
    "vous comprenez": "je comprends",
    "vous": "je",

    "mon": "votre",
    "ma": "votre",
    "mes": "vos",
    "moi": "vous",
    "le mien": "le vôtre",
    "la mienne": "la vôtre",
    "les miens": "les vôtres",
    "les miennes": "les vôtres",

    "votre": "mon",
    "vos": "mes",
    "le vôtre": "le mien",
    "la vôtre": "la mienne",
    "les vôtres": "les miens",

    "nous sommes": "vous êtes",
    "nous avons": "vous avez",
    "nous voulons": "vous voulez",
    "nous souhaitons": "vous souhaitez",
    "nous pouvons": "vous pouvez",
    "nous": "vous",

    "notre": "votre",
    "nos": "vos",
    "leur": "votre",
    "leurs": "vos",

    "tu es": "je suis",
    "tu as": "j'ai",
    "tu peux": "je peux",
    "tu veux": "je veux",
    "tu": "je",
    "ton": "mon",
    "ta": "ma",
    "tes": "mes"
}


# ============================================================
# 115 PAIRES SUR LE CLUB ENIAC
# ============================================================

pairs = [

    # ---------------- SALUTATIONS ----------------

    # 1
    [
        r"^(bonjour|salut|hello|coucou|bonsoir)[.! ]*$",
        [
            "Bonjour ! Bienvenue chez ENIAC. Comment puis-je vous aider ?",
            "Bonjour ! Que souhaitez-vous savoir sur le club ENIAC ?"
        ]
    ],

    # 2
    [
        r"^(bonjour|salut|bonsoir) eniac[.! ]*$",
        ["Bonjour ! Toute l’équipe ENIAC vous souhaite la bienvenue."]
    ],

    # 3
    [
        r"^(ça va|comment vas-tu|comment allez-vous)[? ]*$",
        ["Je vais très bien, merci ! Que souhaitez-vous savoir sur ENIAC ?"]
    ],

    # 4
    [
        r"^(merci|merci beaucoup|je vous remercie)[.! ]*$",
        [
            "Avec plaisir !",
            "Je vous en prie. Avez-vous une autre question sur ENIAC ?"
        ]
    ],

    # 5
    [
        r"^(au revoir|à bientôt|bye|quitter|fin)[.! ]*$",
        ["Au revoir ! À bientôt dans les prochaines activités d’ENIAC."]
    ],

    # ---------------- IDENTITÉ DU CHATBOT ----------------

    # 6
    [
        r"^(qui es-tu|tu es qui|présente-toi)[? ]*$",
        ["Je suis l’assistant virtuel du club ENIAC de l’ENSA Safi."]
    ],

    # 7
    [
        r"^(quel est ton rôle|à quoi sers-tu)[? ]*$",
        ["Je réponds aux questions générales concernant ENIAC, ses activités et ses événements."]
    ],

    # 8
    [
        r"^(es-tu un humain|es-tu une personne)[? ]*$",
        ["Non, je suis un chatbot conçu pour fournir des informations sur ENIAC."]
    ],

    # 9
    [
        r"^(qui t'a créé|qui vous a créé)[? ]*$",
        ["J’ai été conçu pour représenter le club ENIAC et faciliter l’accès à ses informations."]
    ],

    # 10
    [
        r"^(que peux-tu faire|quelles sont tes fonctionnalités)[? ]*$",
        ["Je peux présenter ENIAC et répondre aux questions sur ses activités, son recrutement et ses événements."]
    ],

    # ---------------- PRÉSENTATION D’ENIAC ----------------

    # 11
    [
        r"^(qu'est-ce que|c'est quoi|présente-moi) (le club )?eniac[? ]*$",
        ["ENIAC est un club étudiant de l’ENSA Safi consacré à l’informatique, à la technologie et à l’innovation."]
    ],

    # 12
    [
        r"^que signifie eniac[? ]*$",
        ["ENIAC est le nom du club. C’est également le nom d’un ordinateur historique."]
    ],

    # 13
    [
        r"^eniac est-il un club informatique[? ]*$",
        ["Oui, ENIAC est un club étudiant orienté vers l’informatique et les nouvelles technologies."]
    ],

    # 14
    [
        r"^eniac appartient à quelle école[? ]*$",
        ["Le club ENIAC appartient à l’ENSA Safi."]
    ],

    # 15
    [
        r"^où se trouve (le club )?eniac[? ]*$",
        ["Le club ENIAC est présent à l’École Nationale des Sciences Appliquées de Safi."]
    ],

    # 16
    [
        r"^quel est (le but|l'objectif|la mission) (du club )?eniac[? ]*$",
        ["ENIAC vise à développer les compétences des étudiants grâce à des activités technologiques, pratiques et collaboratives."]
    ],

    # 17
    [
        r"^quelles sont les valeurs (du club|d'eniac)[? ]*$",
        ["ENIAC valorise l’apprentissage, la collaboration, la créativité, l’innovation et le partage des connaissances."]
    ],

    # 18
    [
        r"^à qui s'adresse (le club )?eniac[? ]*$",
        ["ENIAC s’adresse principalement aux étudiants intéressés par l’informatique, la technologie et l’innovation."]
    ],

    # 19
    [
        r"^pourquoi le nom eniac[? ]*$",
        ["Le nom ENIAC fait référence à un ordinateur important dans l’histoire de l’informatique."]
    ],

    # 20
    [
        r"^eniac est-il seulement pour les informaticiens[? ]*$",
        ["Non. Toute personne motivée par la technologie, l’organisation ou le travail associatif peut s’intéresser au club."]
    ],

    # ---------------- ACTIVITÉS ----------------

    # 21
    [
        r"^quelles (activités|actions) (organise|propose) eniac[? ]*$",
        ["ENIAC organise notamment des formations, des ateliers, des conférences, des compétitions et des activités d’intégration."]
    ],

    # 22
    [
        r"^organisez-vous des formations[? ]*$",
        ["Oui, ENIAC peut organiser des formations dans différents domaines de l’informatique."]
    ],

    # 23
    [
        r"^organisez-vous des ateliers[? ]*$",
        ["Oui, ENIAC organise des ateliers permettant aux participants de pratiquer et d’appliquer leurs connaissances."]
    ],

    # 24
    [
        r"^organisez-vous des conférences[? ]*$",
        ["Oui, ENIAC peut inviter des intervenants pour partager leurs expériences et leurs connaissances."]
    ],

    # 25
    [
        r"^organisez-vous des webinaires[? ]*$",
        ["Oui, le club peut organiser des webinaires avec des experts et des professionnels."]
    ],

    # 26
    [
        r"^organisez-vous des hackathons[? ]*$",
        ["ENIAC peut organiser ou participer à des hackathons et à des compétitions technologiques."]
    ],

    # 27
    [
        r"^organisez-vous des compétitions[? ]*$",
        ["Oui, certaines activités d’ENIAC peuvent prendre la forme de compétitions individuelles ou collectives."]
    ],

    # 28
    [
        r"^organisez-vous des activités d'intégration[? ]*$",
        ["Oui, ENIAC participe aux journées d’intégration avec des activités destinées aux nouveaux étudiants."]
    ],

    # 29
    [
        r"^faites-vous des projets[? ]*$",
        ["Oui, les membres peuvent collaborer sur des projets informatiques et innovants."]
    ],

    # 30
    [
        r"^faites-vous des activités en équipe[? ]*$",
        ["Oui, plusieurs activités encouragent la collaboration, la communication et le travail en équipe."]
    ],

    # ---------------- DOMAINES INFORMATIQUES ----------------

    # 31
    [
        r"^proposez-vous des activités (sur|en) intelligence artificielle[? ]*$",
        ["L’intelligence artificielle peut faire partie des thèmes abordés dans les activités d’ENIAC."]
    ],

    # 32
    [
        r"^proposez-vous des activités (sur|en) développement web[? ]*$",
        ["Le développement web peut être abordé dans des formations, des ateliers ou des projets."]
    ],

    # 33
    [
        r"^proposez-vous des activités (sur|en) cybersécurité[? ]*$",
        ["La cybersécurité peut faire partie des domaines présentés par le club."]
    ],

    # 34
    [
        r"^proposez-vous des activités (sur|en) data science[? ]*$",
        ["La data science peut être abordée selon le programme annuel et les intervenants disponibles."]
    ],

    # 35
    [
        r"^proposez-vous des activités (sur|en) programmation[? ]*$",
        ["Oui, la programmation fait partie des principaux domaines pouvant être abordés par ENIAC."]
    ],

    # 36
    [
        r"^quels langages de programmation enseignez-vous[? ]*$",
        ["Les langages abordés dépendent de chaque formation. Consultez le programme de l’activité concernée."]
    ],

    # 37
    [
        r"^puis-je apprendre à coder avec eniac[? ]*$",
        ["Oui, les formations et les ateliers du club peuvent vous aider à développer vos compétences en programmation."]
    ],

    # 38
    [
        r"^avez-vous des formations pour débutants[? ]*$",
        ["Certaines activités peuvent être accessibles aux débutants. Le niveau requis est indiqué dans chaque annonce."]
    ],

    # 39
    [
        r"^avez-vous des formations avancées[? ]*$",
        ["Certaines formations peuvent avoir un niveau avancé. Vérifiez les prérequis indiqués dans leur description."]
    ],

    # 40
    [
        r"^comment connaître le programme des formations[? ]*$",
        ["Le programme et les prérequis sont communiqués dans l’annonce officielle de chaque formation."]
    ],

    # ---------------- ADHÉSION ET RECRUTEMENT ----------------

    # 41
    [
        r"^comment (rejoindre|intégrer) (le club )?eniac[? ]*$",
        ["Vous pouvez déposer votre candidature pendant la campagne de recrutement annoncée par le club."]
    ],

    # 42
    [
        r"^quand commence le recrutement[? ]*$",
        ["La date du recrutement est annoncée sur les canaux officiels d’ENIAC."]
    ],

    # 43
    [
        r"^le recrutement est-il ouvert[? ]*$",
        ["Je ne peux pas confirmer son état actuel. Consultez la dernière annonce officielle d’ENIAC."]
    ],

    # 44
    [
        r"^qui peut rejoindre (le club )?eniac[? ]*$",
        ["Les conditions précises sont annoncées pendant le recrutement. La motivation et l’intérêt pour les activités du club sont importants."]
    ],

    # 45
    [
        r"^faut-il être étudiant à l'ensa safi[? ]*$",
        ["L’adhésion concerne principalement les étudiants de l’ENSA Safi. Les conditions exactes sont précisées pendant le recrutement."]
    ],

    # 46
    [
        r"^faut-il être expert en informatique[? ]*$",
        ["Non. Il est possible de rejoindre le club pour apprendre, à condition d’être motivé et impliqué."]
    ],

    # 47
    [
        r"^faut-il avoir de l'expérience[? ]*$",
        ["L’expérience peut être utile, mais la motivation, l’engagement et la volonté d’apprendre sont également importants."]
    ],

    # 48
    [
        r"^comment se déroule le recrutement[? ]*$",
        ["Le processus exact est communiqué par le club et peut inclure une candidature ainsi qu’un échange avec son équipe."]
    ],

    # 49
    [
        r"^y a-t-il un entretien[? ]*$",
        ["Cela dépend du processus de recrutement choisi. Les étapes sont précisées dans l’annonce officielle."]
    ],

    # 50
    [
        r"^où trouver le formulaire de recrutement[? ]*$",
        ["Le formulaire est partagé sur les canaux officiels du club lorsqu’une campagne de recrutement est ouverte."]
    ],

    # 51
    [
        r"^l'adhésion est-elle gratuite[? ]*$",
        ["Je ne dispose pas d’une information officielle sur d’éventuels frais. Il faut vérifier auprès du bureau du club."]
    ],

    # 52
    [
        r"^puis-je rejoindre le club en cours d'année[? ]*$",
        ["Cela dépend des décisions du bureau et des périodes de recrutement. Contactez le club pour obtenir une confirmation."]
    ],

    # 53
    [
        r"^quels sont les critères de sélection[? ]*$",
        ["Les critères peuvent inclure la motivation, la disponibilité, l’esprit d’équipe et l’intérêt pour les activités du club."]
    ],

    # 54
    [
        r"^comment préparer mon entretien[? ]*$",
        ["Présentez clairement votre motivation, vos compétences, vos disponibilités et ce que vous souhaitez apporter au club."]
    ],

    # 55
    [
        r"^je veux rejoindre eniac parce que (.*)",
        [
            "C’est intéressant que vous souhaitiez rejoindre ENIAC parce que %1. Présentez cette motivation pendant votre candidature."
        ]
    ],

    # ---------------- MEMBRES ET ORGANISATION ----------------

    # 56
    [
        r"^qui dirige (le club )?eniac[? ]*$",
        ["ENIAC est dirigé par un bureau chargé de coordonner les membres et les activités."]
    ],

    # 57
    [
        r"^qui est la présidente (du club )?eniac[? ]*$",
        ["La présidente d’ENIAC pour l’année 2026-2027 est Meryem Samgaz."]
    ],

    # 58
    [
        r"^quel est le rôle de la présidente[? ]*$",
        ["La présidente représente le club, coordonne le bureau et veille au bon déroulement de ses activités."]
    ],

    # 59
    [
        r"^quel est le rôle du secrétaire général[? ]*$",
        ["Le secrétaire général assure notamment le suivi administratif, la documentation et la coordination interne."]
    ],

    # 60
    [
        r"^quel est le rôle des membres[? ]*$",
        ["Les membres contribuent à la préparation, à l’organisation et à la réalisation des activités du club."]
    ],

    # 61
    [
        r"^comment fonctionne le bureau[? ]*$",
        ["Le bureau répartit les responsabilités et coordonne les décisions ainsi que le programme annuel du club."]
    ],

    # 62
    [
        r"^combien de membres compte eniac[? ]*$",
        ["Je ne dispose pas d’un nombre officiel actualisé. Vous pouvez demander cette information au bureau du club."]
    ],

    # 63
    [
        r"^comment devenir responsable dans le club[? ]*$",
        ["Il faut généralement être actif, sérieux et capable d’assumer les responsabilités confiées par le club."]
    ],

    # 64
    [
        r"^les membres travaillent-ils en équipe[? ]*$",
        ["Oui, le fonctionnement du club repose largement sur la collaboration et la répartition des responsabilités."]
    ],

    # 65
    [
        r"^puis-je aider à organiser un événement[? ]*$",
        ["Oui, les membres peuvent contribuer à la préparation logistique, technique ou communicationnelle des événements."]
    ],

    # ---------------- PARTICIPATION AUX ÉVÉNEMENTS ----------------

    # 66
    [
        r"^comment participer à (une activité|un événement)[? ]*$",
        ["Consultez l’annonce officielle et suivez les modalités d’inscription qui y sont indiquées."]
    ],

    # 67
    [
        r"^où trouver les annonces[? ]*$",
        ["Les annonces sont publiées sur les canaux de communication officiels d’ENIAC."]
    ],

    # 68
    [
        r"^les événements sont-ils ouverts à tous[? ]*$",
        ["Cela dépend de l’événement. Le public concerné est précisé dans chaque annonce."]
    ],

    # 69
    [
        r"^les événements sont-ils gratuits[? ]*$",
        ["Cela dépend de l’événement. Les éventuels frais sont indiqués dans l’annonce officielle."]
    ],

    # 70
    [
        r"^faut-il s'inscrire avant un événement[? ]*$",
        ["Si une inscription est nécessaire, le formulaire et la date limite sont indiqués dans l’annonce."]
    ],

    # 71
    [
        r"^puis-je participer sans être membre[? ]*$",
        ["Oui pour certaines activités ouvertes au public. Il faut vérifier les conditions de l’événement concerné."]
    ],

    # 72
    [
        r"^où se déroulent les activités[? ]*$",
        ["Les activités peuvent se dérouler à l’ENSA Safi ou en ligne, selon le format annoncé."]
    ],

    # 73
    [
        r"^quand aura lieu le prochain événement[? ]*$",
        ["Je ne peux pas confirmer une date sans annonce officielle récente. Consultez les canaux du club."]
    ],

    # 74
    [
        r"^combien de temps dure une formation[? ]*$",
        ["La durée dépend de la formation et doit être indiquée dans son programme."]
    ],

    # 75
    [
        r"^donnez-vous des certificats[? ]*$",
        ["Des certificats peuvent être remis selon l’activité. Cette information est précisée dans l’annonce concernée."]
    ],

    # ---------------- NEXUS: THE CODE HUNT ----------------

    # 76
    [
        r"^(qu'est-ce que|c'est quoi) nexus( the code hunt)?[? ]*$",
        ["NEXUS: THE CODE HUNT est un parcours de missions organisé par ENIAC dans le cadre des journées d’intégration."]
    ],

    # 77
    [
        r"^quel est le principe de nexus[? ]*$",
        ["Les équipes suivent un parcours, réalisent des missions et collectent les éléments nécessaires pour former un code final."]
    ],

    # 78
    [
        r"^combien d'équipes participent à nexus[? ]*$",
        ["Le format prévu comprend six équipes."]
    ],

    # 79
    [
        r"^combien de personnes composent une équipe nexus[? ]*$",
        ["Une équipe de NEXUS est composée de trois à quatre participants au maximum."]
    ],

    # 80
    [
        r"^combien de stations contient nexus[? ]*$",
        ["Le parcours prévu comporte six stations."]
    ],

    # 81
    [
        r"^combien de temps dure nexus[? ]*$",
        ["La durée prévue de NEXUS est d’environ une heure."]
    ],

    # 82
    [
        r"^à quelle heure commence nexus[? ]*$",
        ["L’heure de début prévue est 10 h 00."]
    ],

    # 83
    [
        r"^comment gagner nexus[? ]*$",
        ["L’équipe gagnante est la première qui soumet correctement le code final."]
    ],

    # 84
    [
        r"^combien de gagnants y a-t-il dans nexus[? ]*$",
        ["Le format prévoit une seule équipe gagnante."]
    ],

    # 85
    [
        r"^où se déroule nexus[? ]*$",
        ["Le parcours utilise plusieurs espaces de l’ENSA Safi indiqués aux participants pendant l’activité."]
    ],

    # 86
    [
        r"^quelles sont les missions de nexus[? ]*$",
        ["Les missions sollicitent notamment la réflexion, la collaboration, l’observation et la réalisation de défis en équipe."]
    ],

    # 87
    [
        r"^qu'est-ce que le code final de nexus[? ]*$",
        ["Il s’agit d’un code de six chiffres reconstitué grâce aux informations obtenues pendant le parcours."]
    ],

    # 88
    [
        r"^comment soumettre le code de nexus[? ]*$",
        ["À la fin du parcours, l’équipe revient au point de départ pour saisir son identifiant et son code final."]
    ],

    # ---------------- RÉALISATIONS ET PROPOSITIONS ----------------

    # 89
    [
        r"^eniac a-t-il participé à water4future[? ]*$",
        ["Oui. ENIAC a participé à Water4Future 2025 avec le projet Scarabée AquaHarvest 2.0."]
    ],

    # 90
    [
        r"^quel résultat eniac a-t-il obtenu à water4future[? ]*$",
        ["Le projet Scarabée AquaHarvest 2.0 a obtenu la troisième place à Water4Future 2025."]
    ],

    # 91
    [
        r"^qu'est-ce que scarabée aquaharvest 2\.0[? ]*$",
        ["Scarabée AquaHarvest 2.0 est le projet présenté par ENIAC lors de Water4Future 2025."]
    ],

    # 92
    [
        r"^puis-je proposer une activité[? ]*$",
        ["Oui. Vous pouvez présenter une proposition claire au bureau en précisant son objectif, son public et ses besoins."]
    ],

    # 93
    [
        r"^puis-je proposer un projet[? ]*$",
        ["Oui. ENIAC encourage les membres à proposer des projets utiles, réalisables et cohérents avec les objectifs du club."]
    ],

    # 94
    [
        r"^je propose (.*)",
        ["Votre proposition concerne %1. Vous pouvez la structurer avec un objectif, un public cible, un programme et les ressources nécessaires."]
    ],

    # 95
    [
        r"^comment devenir partenaire d'eniac[? ]*$",
        ["Vous pouvez contacter le bureau d’ENIAC et présenter clairement votre organisation ainsi que la collaboration proposée."]
    ],

    # 96
    [
        r"^eniac accepte-t-il les partenariats[? ]*$",
        ["ENIAC peut étudier des propositions de partenariat liées à la formation, à la technologie et aux événements étudiants."]
    ],

    # ---------------- CONTACT ET QUESTIONS LIBRES ----------------

    # 97
    [
        r"^comment contacter (le club )?eniac[? ]*$",
        ["Vous pouvez contacter ENIAC à travers ses canaux officiels ou directement auprès des membres de son bureau."]
    ],

    # 98
    [
        r"^avez-vous (un compte|une page) (instagram|facebook|linkedin)[? ]*$",
        ["Consultez les canaux officiels d’ENIAC pour accéder à ses pages et obtenir les informations les plus récentes."]
    ],

    # 99
    [
        r"^je (veux|souhaite|voudrais) (.*)",
        ["Vous souhaitez %2. Pouvez-vous préciser votre demande concernant ENIAC ?"]
    ],

    # ---------------- HISTOIRE ET FORMATIONS ----------------

    # 100
    [
        r"^(quelle est|donne-moi|donnez-moi) la date de création (du club )?eniac[? ]*$",
        [f"La date de création officielle d’ENIAC est {CLUB_CREATION_DATE}."]
    ],

    # 101
    [
        r"^(quand|en quelle année) (le club )?eniac (a-t-il été|a été|est-il) (créé|fondé)[? ]*$",
        [f"La date de création officielle d’ENIAC est {CLUB_CREATION_DATE}."]
    ],

    # 102
    [
        r"^quelle est l'histoire (du club )?eniac[? ]*$",
        ["ENIAC est un club étudiant de l’ENSA Safi tourné vers l’informatique, l’innovation, l’apprentissage pratique et le partage des connaissances."]
    ],

    # 103
    [
        r"^qui a (créé|fondé) (le club )?eniac[? ]*$",
        ["Le nom des fondateurs doit être confirmé auprès du bureau ou des archives officielles du club."]
    ],

    # 104
    [
        r"^quels types de formations (organisez-vous|propose eniac|proposez-vous)[? ]*$",
        ["ENIAC peut proposer des formations en programmation, développement web, intelligence artificielle, data, cybersécurité et autres domaines numériques, selon le programme annuel."]
    ],

    # 105
    [
        r"^les formations sont-elles (en ligne|à distance|en présentiel)[? ]*$",
        ["Le format dépend de chaque formation : elle peut être organisée en présentiel à l’ENSA Safi ou à distance. L’annonce officielle précise toujours le format retenu."]
    ],

    # 106
    [
        r"^quel niveau faut-il pour suivre une formation[? ]*$",
        ["Le niveau requis dépend du sujet. Certaines formations sont accessibles aux débutants, tandis que d’autres demandent des prérequis indiqués dans l’annonce."]
    ],

    # 107
    [
        r"^comment s'inscrire (à|aux) (une )?formation(s)?[? ]*$",
        ["Lorsqu’une inscription est nécessaire, ENIAC publie un formulaire avec les conditions, les places disponibles et la date limite."]
    ],

    # 108
    [
        r"^qui anime les formations[? ]*$",
        ["Selon le thème, les formations peuvent être animées par des membres compétents, des enseignants, des professionnels ou des experts invités."]
    ],

    # 109
    [
        r"^les formations contiennent-elles de la pratique[? ]*$",
        ["ENIAC privilégie des formations utiles et peut intégrer des démonstrations, des exercices, des ateliers ou de petits projets pratiques."]
    ],

    # 110
    [
        r"^reçoit-on un support (de cours|de formation)[? ]*$",
        ["La disponibilité d’un support dépend du formateur et de la formation. Cette information doit être précisée pendant la séance ou dans l’annonce."]
    ],

    # 111
    [
        r"^les places (pour les formations )?sont-elles limitées[? ]*$",
        ["Elles peuvent être limitées selon la capacité de la salle, le matériel disponible et le format pédagogique choisi."]
    ],

    # 112
    [
        r"^comment proposer (une formation|un sujet de formation)[? ]*$",
        ["Vous pouvez transmettre au bureau le thème, le niveau visé, les objectifs, la durée souhaitée et le public concerné."]
    ],

    # 113
    [
        r"^où consulter le calendrier des formations[? ]*$",
        ["Le calendrier des formations est communiqué à travers les annonces et les canaux officiels d’ENIAC."]
    ],

    # 114
    [
        r"^quels sont les avantages des formations eniac[? ]*$",
        ["Elles permettent de découvrir des technologies, de pratiquer, d’échanger avec des intervenants et de développer des compétences utiles aux projets académiques et personnels."]
    ],

    # 115 — réponse de secours : doit rester la dernière
    [
        r"^(.*)$",
        [
            "Je n’ai pas encore une réponse fiable à cette question. Pouvez-vous la reformuler ?",
            "Je préfère ne pas inventer d’information. Posez-moi une question sur ENIAC, ses activités, son recrutement ou NEXUS.",
            "Cette information doit être confirmée auprès du bureau ou sur les canaux officiels d’ENIAC."
        ]
    ]
]

chat = Chat(pairs, reflections_eniac)


# ============================================================
# INTERFACE STREAMLIT
# ============================================================

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 5%, rgba(92, 82, 205, .20), transparent 28%),
                radial-gradient(circle at 90% 8%, rgba(19, 184, 166, .13), transparent 25%),
                #070b18;
            color: #f8fafc;
        }

        [data-testid="stHeader"] { background: transparent; }

        .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .eniac-card, .login-card {
            padding: 1.7rem;
            border: 1px solid rgba(148, 163, 184, .22);
            border-radius: 24px;
            background: rgba(15, 23, 42, .82);
            box-shadow: 0 20px 55px rgba(0, 0, 0, .28);
            backdrop-filter: blur(14px);
            margin-bottom: 1.2rem;
        }

        .login-card {
            max-width: 510px;
            margin: 5vh auto 1.2rem;
            padding: 2rem;
        }

        .eniac-badge {
            display: inline-block;
            padding: .35rem .75rem;
            border-radius: 999px;
            background: rgba(99, 102, 241, .18);
            color: #c7d2fe;
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
        }

        .eniac-title {
            margin: .8rem 0 .35rem;
            font-size: clamp(2rem, 5vw, 3.4rem);
            line-height: 1.05;
            color: #ffffff;
        }

        .eniac-subtitle {
            color: #cbd5e1;
            font-size: 1rem;
            line-height: 1.7;
            margin: 0;
        }

        .status-online { color: #5eead4; font-weight: 600; }

        div[data-testid="stChatMessage"] {
            border: 1px solid rgba(148, 163, 184, .16);
            border-radius: 18px;
            padding: .35rem .65rem;
            background: rgba(15, 23, 42, .62);
        }

        div[data-testid="stChatInput"] {
            border: 1px solid rgba(129, 140, 248, .45);
            border-radius: 16px;
            background: rgba(15, 23, 42, .94);
        }

        .stButton > button,
        .stFormSubmitButton > button {
            width: 100%;
            border: 0;
            border-radius: 12px;
            color: white;
            font-weight: 700;
            background: linear-gradient(90deg, #4f46e5, #7c3aed);
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            color: white;
            border: 0;
            box-shadow: 0 8px 25px rgba(99, 102, 241, .35);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def check_credentials(username, password):
    """Compare les identifiants sans exposer directement leur valeur."""
    return hmac.compare_digest(username, APP_USERNAME) and hmac.compare_digest(
        password, APP_PASSWORD
    )


def show_login():
    """Affiche l'écran de connexion."""
    st.markdown(
        """
        <div class="login-card">
            <span class="eniac-badge">Espace sécurisé</span>
            <h1 class="eniac-title">Assistant ENIAC</h1>
            <p class="eniac-subtitle">
                Connectez-vous pour accéder au chatbot du club ENIAC
                de l’ENSA Safi.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Nom d’utilisateur",
            placeholder="Saisissez votre identifiant",
        )
        password = st.text_input(
            "Mot de passe",
            type="password",
            placeholder="Saisissez votre mot de passe",
        )
        submitted = st.form_submit_button("Se connecter", use_container_width=True)

    if submitted:
        if check_credentials(username.strip(), password):
            st.session_state.authenticated = True
            st.session_state.username = username.strip()
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": (
                        "Bonjour ! Je suis l’assistant ENIAC. Posez-moi une question "
                        "sur le club, ses formations, ses activités ou NEXUS."
                    ),
                }
            ]
            st.rerun()
        else:
            st.error("Nom d’utilisateur ou mot de passe incorrect.")


def show_chatbot():
    """Affiche l'espace principal du chatbot."""
    with st.sidebar:
        st.markdown("### 🚀 ENIAC Assistant")
        st.caption(f"Connecté en tant que **{st.session_state.username}**")
        st.markdown("---")
        st.markdown("**Thèmes disponibles**")
        st.markdown(
            "- Présentation du club\n"
            "- Formations et activités\n"
            "- Recrutement et adhésion\n"
            "- NEXUS: THE CODE HUNT\n"
            "- Réalisations d’ENIAC"
        )

        if st.button("Se déconnecter", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.messages = []
            st.rerun()

    st.markdown(
        """
        <div class="eniac-card">
            <span class="eniac-badge">Club informatique · ENSA Safi</span>
            <h1 class="eniac-title">Explorez l’univers ENIAC</h1>
            <p class="eniac-subtitle">
                Votre assistant pour découvrir le club, ses formations, ses
                événements, son recrutement et ses projets.
                <span class="status-online">● Assistant en ligne</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    suggestion_columns = st.columns(3)
    suggestions = [
        "Quelles formations proposez-vous ?",
        "Comment rejoindre ENIAC ?",
        "Qu’est-ce que NEXUS ?",
    ]

    selected_suggestion = None
    for column, suggestion in zip(suggestion_columns, suggestions):
        with column:
            if st.button(suggestion, use_container_width=True):
                selected_suggestion = suggestion

    for message in st.session_state.messages:
        avatar = "🚀" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    typed_message = st.chat_input("Écrivez votre question sur ENIAC…")
    user_message = selected_suggestion or typed_message

    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})

        with st.chat_message("user", avatar="👤"):
            st.markdown(user_message)

        response = chat.respond(user_message)
        if not response:
            response = "Je n’ai pas compris votre question. Pouvez-vous la reformuler ?"

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        with st.chat_message("assistant", avatar="🚀"):
            st.markdown(response)


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.authenticated:
    show_chatbot()
else:
    show_login()
