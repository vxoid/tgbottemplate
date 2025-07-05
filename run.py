from aiogram import Router

from bot import dp, main
import logging

from handlers.user.start import start_router

logging.basicConfig(level=logging.INFO)

main_router = Router()
main_router.include_router(start_router)
dp.include_router(main_router)

if __name__ == '__main__':
    main()