import argparse
import json

from .service_api import OneFormServiceAPI


def main():
    parser = argparse.ArgumentParser(description="Load missing-nodes bundle into DB draft")
    parser.add_argument("--bundle-file", required=True)
    parser.add_argument("--form-type", default="ITR6_BASIC")
    parser.add_argument("--actor", default="bundle_loader")
    parser.add_argument("--activate", action="store_true")
    args = parser.parse_args()

    with open(args.bundle_file, "r", encoding="utf-8") as f:
        bundle = json.load(f)

    nodes = bundle.get("nodes", {})
    rules = bundle.get("__rules__", {})

    api = OneFormServiceAPI(form_type=args.form_type, actor=args.actor)
    draft_id = api.create_draft_from_active()

    api.update_node(draft_id, "__rules__", rules)
    for node_name, node_def in nodes.items():
        api.update_node(draft_id, node_name, node_def)

    report = api.validate(draft_id)
    print(f"draft_id={draft_id} valid={report.get('valid')} errors={len(report.get('errors', []))}")
    if report.get("errors"):
        print("Top errors:")
        for err in report["errors"][:10]:
            print(f"- {err}")

    if args.activate and report.get("valid"):
        api.activate(draft_id)
        print(f"Activated draft_id={draft_id}")
    elif args.activate:
        print("Activation skipped because validation failed.")


if __name__ == "__main__":
    main()
