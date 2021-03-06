from webpay.base.utils import invert

# These come from solitude. Go there for detailed comments.
SOURCE_BANGO = 1

TYPE_PAYMENT = 0
TYPE_REFUND = 1
TYPE_REVERSAL = 2

STATUS_PENDING = 0
STATUS_COMPLETED = 1
STATUS_CHECKED = 2
STATUS_RECEIVED = 3
STATUS_FAILED = 4  # Failed at the payment provider.
STATUS_CANCELLED = 5
STATUS_STARTED = 6
STATUS_ERRORED = 7  # Failed at the Mozilla end.

STATUS_ENDED = (STATUS_COMPLETED, STATUS_FAILED, STATUS_CANCELLED,
                STATUS_ERRORED)
STATUS_RETRY_OK = (STATUS_FAILED, STATUS_CANCELLED)

ACCESS_PURCHASE = 1
ACCESS_SIMULATE = 2

PROVIDER_BANGO = 1
PROVIDER_REFERENCE = 2
PROVIDER_BOKU = 3

# These are constants for Solitude but not necessarily for Webpay.
# See PAYMENT_PROVIDER in settings.
PROVIDERS = {
    'bango': PROVIDER_BANGO,
    'reference': PROVIDER_REFERENCE,
    'boku': PROVIDER_BOKU
}

PROVIDERS_INVERTED = dict(invert(PROVIDERS))
