import logging
import asyncio
from loader import *
import handlers.users.start
import handlers.users.run
import handlers.users.rozdely
import handlers.users.test_rozdel_mech
import handlers.users.test_rozdel_molek
import handlers.users.test_rozdel_elekdyn
import handlers.users.test_rozdel_koleb
import handlers.users.test_rozdel_optyka
import handlers.users.test

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())