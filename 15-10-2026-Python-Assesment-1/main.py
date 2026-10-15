# Q57. Import the module.
import retail_utils



# Q58. Call all three functions.
total = retail_utils.calculate_order_total(2500, 4)

discount = retail_utils.calculate_discount(total)

stock_status = retail_utils.check_stock(15)
print("Q58 - Order Total:", total)
print("Q58 - Discount:", discount)
print("Q58 - Stock Status:", stock_status)



# Q59. Import one function directly.
from retail_utils import calculate_order_total

print(
    "Q59 - Direct Function:",
    calculate_order_total(1200, 3)
)


# Q60. Import module using an alias.
import retail_utils as ru
print("Q60 - Alias Import:", ru.check_stock(0))


