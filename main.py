from sys import stdout

from app_logic.get_instruments import create_df_instruments


if __name__ == '__main__':
    data = create_df_instruments()
    data.to_csv(stdout, index=False)
