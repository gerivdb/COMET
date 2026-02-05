# Écosystème GitHub gerivdb

## Vue d'ensemble
- **Total des dépôts**: 109
- **Publics**: 2 (email-sender-1 + 1 autre)
- **Privés**: 108
- **Dernière mise à jour**: 25 octobre 2025

## Dépôts Principaux (Non-Lovable)

### DevTools
- **URL**: https://github.com/gerivdb/DevTools
- **Langage**: PowerShell
- **Taille**: 290 KB
- **Issues ouvertes**: 8
- **Description**: Outils de développement et automatisation PowerShell
- **Statut**: Privé, activement maintenu

### FLUENCE
- **URL**: https://github.com/gerivdb/FLUENCE
- **Langage**: Go
- **Description**: Écosystème d'exécution cognitif centré sur la logique ternaire-floue, optimisé pour la performance DevTools
- **Architecture**: Go/Rust/Python hybride avec IA contextuelle
- **Statut**: Privé, récemment créé (octobre 2025)

### ECOYSTEM
- **URL**: https://github.com/gerivdb/ECOYSTEM
- **Langage**: PowerShell
- **Taille**: 276 KB
- **Issues ouvertes**: 1
- **Description**: Écosystème principal de gestion et orchestration
- **Statut**: Privé, activement développé

### Email/Communication
- **email-sender-1**: Public, PowerShell, licence MIT
  - URL: https://github.com/gerivdb/email-sender-1
  - Taille: 744 KB
  - Issues: 2 ouvertes
- **email-sender-2**: Privé, PowerShell (7 KB)

### IA/Recherche
- **BRAIN**: Privé, Python (380 KB)
- **BRAIN-DOCS**: Privé, HTML (256 B)
- **zen-mcp-modified**: Privé, PowerShell (750 KB) - MCP modifié avec Go workspace

### Projets Métier
- **CANDIDATOR**: Python - Outils de candidature et manipulation CV
- **BANK-BUSTER**: Python - Audit financier et contestation frais bancaires
- **GERIBOOKING**: TypeScript - Solutions de réservation
- **racines**: Python - Reconstitution biographique

### Automation/Factory
- **TOOL-FACTORY-1**: Python (7 KB, 1 issue)
- **CLIP-FACTORY**: Python (732 B)
- **PITCH-1**: Python (8.4 KB, 2 issues)

## Dépôts CMS Lovable (~70 dépôts)

Pattern de nommage: `geri-cms-*` avec variations temporelles
- Exemples: `geri-cms-2-07-36-31`, `geri-cms-3-g16-v01`, `geri-cms-2-09-18-81-cbe1d349`
- Principalement TypeScript
- Tous privés
- À exclure des workflows génériques DEV COMET

## Répartition par Langage

### PowerShell (5 projets)
- DevTools, ECOYSTEM, email-sender-1, email-sender-2, zen-mcp-modified

### Python (7 projets)
- BRAIN, CANDIDATOR, BANK-BUSTER, TOOL-FACTORY-1, CLIP-FACTORY, PITCH-1, racines

### TypeScript (5+ projets)
- GERIBOOKING, geri-book-cloner, stage-craft-control-hub, geri12cmsv74, geri-cms-*

### Go (1 projet)
- FLUENCE

### HTML (1 projet)
- BRAIN-DOCS

## Intégrations DEV COMET

### GitHub MCP Tools
Priorité sur les dépôts principaux :
```bash
gerivdb/DevTools      # PowerShell automation
gerivdb/FLUENCE       # Go orchestration  
gerivdb/ECOYSTEM      # PowerShell ecosystem
gerivdb/BRAIN         # Python IA
gerivdb/email-sender-1 # Public PowerShell
```

### Comet Browser Navigation
Cibles pour extraction automatique :
- README.md et documentation
- Issues et discussions
- Commits récents et releases
- Dépendances inter-projets

### Filtrage Lovable
Exclusion pattern : `NOT repo:geri-cms*` dans toutes les requêtes génériques

## Architecture Recommandée

```
FLUENCE (Orchestrateur Go)
    ├── DevTools (PowerShell automation)
    ├── ECOYSTEM (PowerShell management) 
    ├── BRAIN (Python IA)
    └── Projets Métier (Python/TypeScript)
```

## Actions Prioritaires

1. **Monitoring DevTools** (8 issues ouvertes à traiter)
2. **Documentation FLUENCE** (nouveau, architecture à clarifier)
3. **Synchronisation ECOYSTEM** (1 issue à investiguer)
4. **Archivage CMS Lovable** (considérer cleanup des anciens)

## Notes Importantes

- 99% des dépôts sont privés (haute confidentialité)
- Architecture multi-langage cohérente
- Forte orientation DevOps et automatisation
- Écosystème mature avec spécialisations métier
- Pattern de nommage temporel sur projets CMS