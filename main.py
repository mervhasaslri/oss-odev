from flask import Flask, jsonify, request

app = Flask(__name__)

# Örnek dizi verileri
diziler = [
    {
        'id': 1,
        'isim': 'Game of Thrones',
        'turu': 'Fantastik',
        'puan': 9.3
    },
    {
        'id': 2,
        'isim': 'Vikings',
        'turu': 'Tarihî',
        'puan': 8.5
    }
]

# Tüm dizileri listeleme endpoint'i
@app.route('/api/diziler', methods=['GET'])
def get_diziler():
    return jsonify(diziler)

# Belirli bir diziye erişme endpoint'i
@app.route('/api/diziler/<int:dizi_id>', methods=['GET'])
def get_dizi(dizi_id):
    dizi = next((dizi for dizi in diziler if dizi['id'] == dizi_id), None)
    if dizi:
        return jsonify(dizi)
    else:
        return jsonify({'mesaj': 'Dizi bulunamadı'}), 404

# Yeni dizi ekleme endpoint'i
@app.route('/api/diziler', methods=['POST'])
def add_dizi():
    yeni_dizi = request.json
    if 'isim' in yeni_dizi and 'turu' in yeni_dizi and 'puan' in yeni_dizi:
        yeni_dizi['id'] = len(diziler) + 1
        diziler.append(yeni_dizi)
        return jsonify({'mesaj': 'Yeni dizi eklendi', 'dizi': yeni_dizi}), 201
    else:
        return jsonify({'mesaj': 'Eksik bilgi', 'örnek': {'isim': 'Dizi İsmi', 'turu': 'Dizi Türü', 'puan': 'Dizi Puanı'}}), 400

# Dizi güncelleme endpoint'i
@app.route('/api/diziler/<int:dizi_id>', methods=['PUT'])
def update_dizi(dizi_id):
    dizi = next((dizi for dizi in diziler if dizi['id'] == dizi_id), None)
    if not dizi:
        return jsonify({'mesaj': 'Dizi bulunamadı'}), 404
    else:
        data = request.json
        if 'isim' in data:
            dizi['isim'] = data['isim']
        if 'turu' in data:
            dizi['turu'] = data['turu']
        if 'puan' in data:
            dizi['puan'] = data['puan']
        return jsonify({'mesaj': 'Dizi güncellendi', 'dizi': dizi})

# Dizi silme endpoint'i
@app.route('/api/diziler/<int:dizi_id>', methods=['DELETE'])
def delete_dizi(dizi_id):
    global diziler
    dizi = next((dizi for dizi in diziler if dizi['id'] == dizi_id), None)
    if not dizi:
        return jsonify({'mesaj': 'Dizi bulunamadı'}), 404
    else:
        diziler = [d for d in diziler if d['id'] != dizi_id]
        return jsonify({'mesaj': 'Dizi silindi', 'silinen_dizi': dizi})

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # 8000 numaralı portta çalıştır
