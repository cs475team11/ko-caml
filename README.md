## Introduction
This project is based on the [guidance for EIF matching on aws](https://github.com/aws-solutions-library-samples/guidance-for-environmental-impact-factor-mapping-on-aws?tab=readme-ov-file). We replicated the original pipeline provided by AWS and explored the impact of the language and cultural barriers on the performance of EIF matching. 


## Datasets
### Benchmark
1. Annotations
2. Model Results
3. Evaluation

### Input data
1. **Product Names** [[folder](https://github.com/cs475team11/ko-caml/tree/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/product_names)]
    - Original
        - Amazon Products Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/product_names/amazon_product_names_groceries_eng.csv)] [[source](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset?select=All+Grocery+and+Gourmet+Foods.csv)]
        - Coupang Products Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/product_names/coupang_product_names_groceries_v3_kor.csv)]
    - Translated
        - Amazon Products Dataset (Korean) [[data](https://github.com/cs475team11/ko-caml/blob/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/input/amazon_product_names_groceries_kor.csv)]
        - Coupang Products Dataset (English) [[data](https://github.com/cs475team11/ko-caml/blob/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/input/coupang_product_names_groceries_v3%20eng.csv)]
2. **HS Code Dataset** [[folder](https://github.com/cs475team11/ko-caml/tree/main/guidance_for_environmental_impact_factor_mapping_on_aws/assets/datasets)]
    - Original
        - Global HS Code Dataset: [[source](https://unstats.un.org/unsd/classifications/Econ)]
        - Korean HS Code Dataset: [[source](https://www.data.go.kr/data/15049722/fileData.do?recommendDataYn=Y)]
    - Translated
        - Global

## License

This library is licensed under the Apache-2.0 License. See the LICENSE file.


