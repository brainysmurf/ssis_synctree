from asyncpgsa import pg

class DB:
	""" Adapter class for asyncpgsa """

	async def init(self, settings):
		""" TODO: Errors """
		await pg.init(
		    host=settings['db_host'],
		    port=settings['db_port'],
		    database=settings['db_database'],
		    user=settings['db_user'],
		    # loop=loop,
		    password=settings['db_pass'],
		    min_size=5,
		    max_size=10
		)

	def __call__(self):
		return pg

	def __init__(self):
		loop = asyncio.get_event_loop()
		future = asyncio.ensure_future( self.init() )
		loop.run_until_complete( future )

import sys
sys.modules['db'] = DB()