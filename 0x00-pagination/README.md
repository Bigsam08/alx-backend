# Most endpoints that returns a list of entities will need to have some sort of pagination.

# Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic.

# Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

# Offset Pagination
# This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.

# Limit/Offset Paging would look like GET /items?limit=20&offset=100. This query would return the 20 rows starting with the 100th row.

# Filtering
# URL parameters is the easiest way to add basic filtering to REST APIs. If you have an /items endpoint which are items for sale, you can filter via the property name such as GET /items?state=active or GET /items?state=active&seller_id=1234. However, this only works for exact matches. What if you want to do a range such as a price or date range?
#
# The problem is URL parameters only have a key and a value but filters are composed of three components:

# The property or field name
# The operator such as eq, lte, gte
# The filter value