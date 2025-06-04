import './style.css'
// import 'lucide-static/font/lucide.css'
import Alpine from "alpinejs";
import ajax from '@imacrayon/alpine-ajax'
import mask from "@alpinejs/mask"
import collapse from "@alpinejs/collapse"


Alpine.plugin(mask)
Alpine.plugin(collapse)
Alpine.plugin(ajax)

Alpine.start()