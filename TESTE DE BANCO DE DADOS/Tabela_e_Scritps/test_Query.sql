

SELECT  dc.reg_ans, razao_social, SUM(dc.vl_saldo_final) AS valor_final
FROM demonstracoes_contabeis dc 
JOIN  registro_ans ra ON dc.reg_ans = ra.registro_ans
WHERE dc.descricao LIKE 'Despesas com Eventos/Sinistros%' 
AND dc.data::date >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY dc.reg_ans, ra.razao_social
ORDER BY valor_final DESC
LIMIT 10 ;



SELECT  dc.reg_ans, razao_social, SUM(dc.vl_saldo_final) AS valor_final
FROM demonstracoes_contabeis dc 
JOIN  registro_ans ra ON dc.reg_ans = ra.registro_ans
WHERE dc.descricao LIKE 'Despesas%' 
AND dc.data::date >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY dc.reg_ans, ra.razao_social
ORDER BY valor_final DESC
LIMIT 10 ;

