# LaserLink V7 - Implantação

Ambientes recomendados:
1. Desenvolvimento local
2. Homologação/staging
3. Produção

Antes da distribuição:
- migrar autenticação local para Supabase Auth
- ligar frontend ao banco real
- storage para fotos/documentos
- testes E2E em navegador/dispositivo
- testes de carga e concorrência
- pagamentos sandbox + webhooks
- política de privacidade/termos
- observabilidade, backup e alertas
- remover opção pública de criar administrador
- configurar domínio e HTTPS
