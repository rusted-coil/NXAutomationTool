rem 環境変数 ANACONDA_ROOT: C:\Users\ユーザー\Anaconda3
pushd Scripts
call %ANACONDA_ROOT%\Scripts\activate.bat
call activate NXAutomationTool
python Window.py
popd
