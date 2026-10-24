import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import streamlit as st

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_credentials():
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path or not os.path.exists(creds_path):
        raise RuntimeError("Service account JSON key not found. Set GOOGLE_APPLICATION_CREDENTIALS.")
    return service_account.Credentials.from_service_account_file(creds_path, scopes=SCOPES)

def get_sheets_service():
    return build("sheets", "v4", credentials=get_credentials())

def read_sheet(spreadsheet_id: str, range_name: str = "Sheet1"):
    service = get_sheets_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name
    ).execute()
    return result.get("values", [])

def write_sheet(spreadsheet_id: str, range_name: str, values: list):
    service = get_sheets_service()
    body = {"values": values}
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="USER_ENTERED",
        body=body,
    ).execute()
    return result

def get_sheet_id(index: int):
    env_key = f"GOOGLE_SHEET_ID_{index}"
    sheet_id = os.getenv(env_key)
    if not sheet_id:
        raise RuntimeError(f"Missing {env_key} in .env")
    return sheet_id
