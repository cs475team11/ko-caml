## Introduction
This project is based on the [guidance for EIF matching on aws](https://github.com/aws-solutions-library-samples/guidance-for-environmental-impact-factor-mapping-on-aws?tab=readme-ov-file). We replicated the original pipeline provided by AWS and explored the impact of the language and cultural barriers on the performance of EIF matching. 


## Datasets
### Benchmark
1. **Model Results** [[folder](https://github.com/cs475team11/ko-caml/tree/main/benchmark/results)]
    - Amazon
    - Amazon (Translated to Korean)
    - Coupang
2. **Annotations** [[folder](https://github.com/cs475team11/ko-caml/tree/main/benchmark/gt)]
    - Amazon
    - Coupang
3. **Evaluation** [[folder](https://github.com/cs475team11/ko-caml/tree/main/benchmark/evaluation)]
    - Amazon
    - Amazon (Translated to Korean)
    - Coupang

### Input data
1. **Product Names** [[folder](https://github.com/cs475team11/ko-caml/tree/main/inputs/assets/product_names)]
    - Original
        - Amazon Products Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/product_names/amazon_product_names_groceries_eng.csv)] [[source](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset?select=All+Grocery+and+Gourmet+Foods.csv)]
        - Coupang Products Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/product_names/coupang_product_names_groceries_v3_kor.csv)]
    - Translated
        - Amazon Products Dataset (Korean) [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/product_names/amazon_product_names_groceries_kor.csv)]
2. **HS Code Dataset** [[folder](https://github.com/cs475team11/ko-caml/tree/main/inputs/assets/hs_codes)]
    - Original
        - Global HS Code Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/hs_codes/Filtered_HSCodeandDescription_eng.csv)] [[source](https://unstats.un.org/unsd/classifications/Econ)]
        - Korean HS Code Dataset [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/hs_codes/Korean_HSCode_kor_6digits.csv)] [[source](https://www.data.go.kr/data/15049722/fileData.do?recommendDataYn=Y)]
    - Translated
        - Global HS Code Dataset (Korean) [[data](https://github.com/cs475team11/ko-caml/blob/main/inputs/assets/hs_codes/Filtered_HSCodeandDescription_kor.csv)]

## License

This library is licensed under the Apache-2.0 License. See the LICENSE file.


