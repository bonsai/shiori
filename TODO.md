# TODOリスト

## MVP (Minimum Viable Product)

- [x] 設計ドキュメントの作成 (`STACK.md`, `DESIGN.md`, `TODO.md`)
- [x] プロジェクトのディレクトリ構造と空ファイルの作成
- [ ] `requirements.txt` を作成し、依存ライブラリを管理する
- [ ] コアエンジン (`src/main.py`) の実装
    - [ ] `rag.yaml` の読み込み機能
    - [ ] プラグインの動的ロード機能
    - [ ] パイプライン実行ロジック
- [ ] プラグインの基底クラス (`src/plugins/base.py`) の定義
- [ ] `Subscription::GoogleKeep` プラグインの実装 (`src/plugins/google_keep.py`)
    - [ ] Takeout JSON ファイルの読み込み
    - [ ] `Entry` オブジェクトへの変換
- [ ] `Publish::BigQuery` プラグインのスケルトン実装
    - [ ] BigQueryへの接続とデータ書き込みの雛形作成
- [ ] `Subscription::GoogleKeep` のユニットテスト (`tests/test_google_keep.py`)
    - [ ] テスト用のダミーJSONファイルを用意
    - [ ] ファイル読み込みが正しく行われるかテスト

## v1.1

- [ ] `Filter::LLM::Vectorize` プラグインの実装
- [ ] `Filter::LLM::MetadataEnricher` プラグインの実装
- [ ] `Publish::Gmail` プラグインの実装
- [ ] ロギング機能の強化
- [ ] エラーハンドリングの強化
- [ ] 他の `Subscription` プラグインの実装
