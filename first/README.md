## Arquitetura


### Layers

* Entities:
  * Reflete as tabelas do DB e possúi as regras de negócio
* useCases:
  * Regras de negócio da aplicação, resposável pela comunicação com as entidade,
    toda informação antes de ir deretamenta para as entidades devem passar por essa camada
* Adapters:
  * Faz a tradução dos dados para as camadas mais externas, ex:
    * Controllers
    * Services
    * Presenters
    * Repositories
* Infra:
  * Frameworks e drivers