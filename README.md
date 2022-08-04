# python-snowtrace


[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6db2e36886ee46f58720c6131ef58dd6)](https://app.codacy.com/gh/EmperorMew/python-snowtrace?utm_source=github.com&utm_medium=referral&utm_content=EmperorMew/python-snowtrace&utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/94c15c6d8b1ec869a7fd/maintainability)](https://codeclimate.com/github/EmperorMew/python-snowtrace/maintainability)
![GitHub](https://img.shields.io/github/license/EmperorMew/python-snowtrace)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385/)


A minimal, yet complete, Python API for [Snowtrace.io](https://Snowtrace.io/). 

All standard endpoints are provided.

Available on [PyPI](https://pypi.org/project/python-snowtrace/). Powered by [Snowtrace.io APIs](https://Snowtrace.io/apis#misc).


___


## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://Snowtrace.io/apis#accounts">(source)</a></summary>
<p>

* `get_eth_balance`
* `get_eth_balance_multiple`
* `get_normal_txs_by_address`
* `get_normal_txs_by_address_paginated`
* `get_internal_txs_by_address`
* `get_internal_txs_by_address_paginated`
* `get_internal_txs_by_txhash`
* `get_internal_txs_by_block_range_paginated`
* `get_erc20_token_transfer_events_by_address`
* `get_erc20_token_transfer_events_by_contract_address_paginated`
* `get_erc20_token_transfer_events_by_address_and_contract_paginated`
* `get_erc721_token_transfer_events_by_address`
* `get_erc721_token_transfer_events_by_contract_address_paginated`
* `get_erc721_token_transfer_events_by_address_and_contract_paginated`
* `get_mined_blocks_by_address`
* `get_mined_blocks_by_address_paginated`

</details>

<details><summary>Contracts <a href="https://Snowtrace.io/apis#contracts">(source)</a></summary>
<p>
  
* `get_contract_abi`
* `get_contract_source_code`

</details>



<details><summary>Transactions <a href="https://Snowtrace.io/apis#transactions">(source)</a></summary>
<p>

* `get_tx_receipt_status`

</details>

<details><summary>Blocks <a href="https://Snowtrace.io/apis#blocks">(source)</a></summary>
<p>
  
* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>GETH/Parity Proxy <a href="https://Snowtrace.io/apis#proxy">(source)</a></summary>
<p>

* `get_proxy_block_number`
* `get_proxy_block_by_number`
* `get_proxy_uncle_by_block_number_and_index`
* `get_proxy_block_transaction_count_by_number`
* `get_proxy_transaction_by_hash`
* `get_proxy_transaction_by_block_number_and_index`
* `get_proxy_transaction_count`
* `get_proxy_transaction_receipt`
* `get_proxy_call`
* `get_proxy_code_at`
* `get_proxy_storage_position_at`
* `get_proxy_gas_price`
* `get_proxy_est_gas`

</details>

<details><summary>Tokens <a href="https://Snowtrace.io/apis#tokens">(source)</a></summary>
<p>
  
* `get_total_supply_by_contract_address`
* `get_acc_balance_by_token_and_contract_address`

</details>

<details><summary>Stats <a href="https://Snowtrace.io/apis#stats">(source)</a></summary>
<p>
  
* `get_total_eth_supply`

</details>

*If you think that a newly-added method is missing, kindly open an [issue](https://github.com/EmperorMew/python-snowtrace/issues) as a feature request and I will do my best to add it.*

## Installation

Before proceeding, you should register an account on [Snowtrace.io](https://Snowtrace.io/) and [generate a personal API key](https://Snowtrace.io/myapikey) to use. 

Install from source:

``` bash
pip install git+https://github.com/EmperorMew/python-snowtrace.git
```

Alternatively, install from [PyPI](https://pypi.org/project/python-snowtrace/):

```bash
pip install python-snowtrace
```

## Unit tests

In `bash`, test that everything looks OK on your end using your `YOUR_API_KEY` (without quotation marks) before proceeding:

``` bash
bash run_tests.sh YOUR_API_KEY
````

This will regenerate the logs under `logs/` with the most recent results and the timestamp of the execution.

The tests also include the PRO endpoints so if your key is not PRO, the correspondings tests are expected to fail.

## Usage

In `python`, create a client with your personal [Snowtrace.io](https://Snowtrace.io/) API key:

``` python
from etherscan import Snowtrace
avax = Snowtrace(YOUR_API_KEY) # key in quotation marks
```

Then you can call all available methods, e.g.:

``` python
avax.get_eth_balance(address="0x316c15213B097854a0c31565a0eC8705f6f9e72B")

> ''
```

## Examples

Examples (arguments and results) for all methods may be found as JSON files [here](https://github.com/EmperorMew/python-snowtrace/tree/master/logs).  For example, if you want to use the method `get_block_number_by_timestamp`, you can find the supported arguments and the format of its output in its respective [JSON file](logs/standard/get_block_number_by_timestamp.json):

``` json
{
  "method": "get_block_number_by_timestamp",
  "module": "blocks",
  "kwargs": {
    "timestamp": "1578638524",
    "closest": "before"
  },
  "log_timestamp": "2020-10-28-12:34:44",
  "res": "9251482"
}
```

where `kwargs` refer to the required named arguments and `res` refers to the expected result if you were to run:

``` python
avax.get_block_number_by_timestamp(timestamp="1578638524", closest="before")

> '9251482'
```

**Disclaimer**: Those examples blindly use the arguments originally showcased [here](https://api.Snowtrace.io/apis) and the selected wallets/contracts do not reflect any personal preference. You should refer to the same source for additional information regarding specific argument values.

## Issues

For problems regarding installing or using the package please open an [issue](https://github.com/EmperorMew/python-snowtrace/issues). Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

## Cite

DRP, EmperorMew/python-snowtrace. *https://github.com/EmperorMew/python-snowtrace (2022)*.


Feel free to leave a :star: if you found this package useful.

___

 Powered by [Snowtrace.io APIs](https://Snowtrace.io/apis).
