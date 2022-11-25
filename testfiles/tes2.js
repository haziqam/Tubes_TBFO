const bankTransfer = (req) => {
    let data;
    let body = req.body;

    let bankTransfer = new PaymentMethods(body.items, customer);

    switch (body.channel) {
        case "BCA":
            data = bankTransfer.bca();
            break;
        case "BNI":
            data = bankTransfer.bni();
            break;
        case "BRI":
            data = bankTransfer.bri();
            break;
        case "MANDIRI":
            data = bankTransfer.mandiri();
            break;
        case "PERMATA":
            data = bankTransfer.permata();
            break;
    }
  
    return data;
};