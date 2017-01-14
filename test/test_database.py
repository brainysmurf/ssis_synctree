"""

"""
import asyncio
from ssis_synctree import db
import sqlalchemy as sa
import gns


async def db_continue():

	gns.set_debug(True)

	query = sa.select('*') \
		.select_from(sa.text('ssismdl_user as u')) \
		.where(sa.text('u.firstname = :first_name')) \
		.params(first_name='Adam')
	me = await db().fetch(query)
	gns.tutorial(f"Got 'me' {me}", banner=True)

	# pool = await asyncpgsa.create_pool(
	#     host=settings['db_host'],
	#     port=settings['db_port'],
	#     database=settings['db_database'],
	#     user=settings['db_user'],
	#     # loop=loop,
	#     password=settings['db_pass'],
	#     min_size=5,
	#     max_size=10,
	# )

def test_async():
	loop = asyncio.get_event_loop()
	future = asyncio.ensure_future( db_continue() )
	loop.run_until_complete( future )

if __name__ == "__main__":
		test_async()