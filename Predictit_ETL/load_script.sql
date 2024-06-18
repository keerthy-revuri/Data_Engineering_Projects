
truncate table  postgres.public.predictit;

copy postgres.public.predictit(
	image,
	name,
	shortName,
	status,
	lastTradePrice,
	bestBuyYesCost,
	bestBuyNoCost,
	bestSellYesCost,
	bestSellNoCost,
	lastClosePrice,
	displayOrder,
	updated_time,
	market_id,
	market_url,
	contract_id,
	new_image
)
FROM 'C:/Users/Public/dataeng_project_output/output.csv'
DELIMITER ','
CSV HEADER;

DELETE FROM postgres.public.predictit where contract_id is null;

DELETE FROM postgres.public.predict_it_target using postgres.public.predictit where predictit.contract_id = predict_it_target.contract_id
and predictit.market_id = predict_it_target.market_id;

drop table if exists temp_predictit;

create temporary table temp_predict_it
as SELECT image,
	name,
	shortName,
	status,
	lastTradePrice,
	bestBuyYesCost,
	bestBuyNoCost,
	bestSellYesCost,
	bestSellNoCost,
	lastClosePrice,
	displayOrder,
	updated_time,
	market_id,
	market_url,
	contract_id,
	new_image,
	split_part(image, '/', -1) as png_image
FROM postgres.public.predictit;

INSERT INTO postgres.public.predict_it_target(
    image,
	name,
	shortName,
	status,
	lastTradePrice,
	bestBuyYesCost,
	bestBuyNoCost,
	bestSellYesCost,
	bestSellNoCost,
	lastClosePrice,
	displayOrder,
	updated_time,
	market_id,
	market_url,
	contract_id,
	new_image,
	png_image,
	created_by,
    created_dt,
    updated_by,
    updated_dt)
SELECT image,
	name,
	shortName,
	status,
	lastTradePrice,
	bestBuyYesCost,
	bestBuyNoCost,
	bestSellYesCost,
	bestSellNoCost,
	lastClosePrice,
	displayOrder,
	updated_time,
	market_id,
	market_url,
	contract_id,
	new_image,
	 png_image,
	'Keerthy',
	CURRENT_TIMESTAMP,
	'Keerthy',
	CURRENT_TIMESTAMP
FROM temp_predict_it

