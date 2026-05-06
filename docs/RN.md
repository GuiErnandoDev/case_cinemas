# Regras de Negócio (RN)

### RN01 — Intervalo entre Sessões
O sistema não deve permitir o agendamento de sessões no mesmo cinema com intervalo inferior a 15 minutos entre o término de um filme e o início do próximo.

### RN02 — Limite de Lotação
O registro de público para uma sessão não pode, em hipótese alguma, ultrapassar a capacidade máxima de público definida no cadastro do cinema correspondente.

### RN03 — Coerência de Horários
O sistema deve impedir o cadastro de sessões cujo horário de início seja anterior ao horário atual (sessões retroativas) ou que conflitem com horários de limpeza da sala.

### RN04 — Consistência de Relatórios
A totalização de público por filme ou cinema deve ser calculada em tempo real, baseando-se exclusivamente nos registros confirmados de cada sessão individual.
