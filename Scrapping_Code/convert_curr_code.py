
#Currency Symbol to Currency Code Conversion
def convert_curr_codes(symbol):
    currency_dict = {
    '$': 'USD', 'AUA$': 'AUD', 'CAC$': 'USD', '€': 'EUR', '¥': 'JPY', '£': 'GBP', 'CAD$': 'CAD', 'CHF': 'CHF',
    '元': 'CNY', 'kr': 'SEK', 'NZ$': 'NZD', '₱': 'PHP', 'zł': 'PLN', '฿': 'THB', '₩': 'KRW', '₽': 'RUB', '₹': 'INR',
    'R$': 'BRL', 'R': 'ZAR', 'RM': 'MYR', 'Rp': 'IDR', '₫': 'VND', '﷼': 'IRR', '₪': 'ILS', '₫': 'VND', '₮': 'MNT', '₦': 'NGN',
    'Kč': 'CZK', 'Ft': 'HUF', '₸': 'KZT', 'د.إ': 'AED', '₴': 'UAH', '₺': 'TRY', '₼': 'AZN', '₩': 'KRW', '₭': 'LAK', '₲': 'PYG', '₡': 'CRC', '₤': 'TRL',
    'MX$': 'MXN', 'S$': 'SGD'
    #Add more to get rid of Unknown Values
    }
    return currency_dict.get(symbol, 'Unknown')

