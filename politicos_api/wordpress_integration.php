<?php
/**
 * Plugin Name: Candidatos Políticos API
 * Description: Integración con la API de candidatos políticos
 * Version: 1.0
 * Author: Tu Nombre
 */

// Registrar shortcode para mostrar candidatos
function candidatos_shortcode($atts) {
    $atts = shortcode_atts(array(
        'cargo' => '',
        'partido' => '',
    ), $atts);
    
    // URL de la API
    $api_url = 'https://tu-api-railway.app/api/candidatos/';
    
    // Parámetros de búsqueda
    $params = array();
    if (!empty($atts['cargo'])) {
        $params['search'] = $atts['cargo'];
    }
    if (!empty($atts['partido'])) {
        $params['search'] = $atts['partido'];
    }
    
    // Construir URL con parámetros
    if (!empty($params)) {
        $api_url .= '?' . http_build_query($params);
    }
    
    // Realizar la solicitud a la API
    $response = wp_remote_get($api_url);
    
    if (is_wp_error($response)) {
        return 'Error al conectar con la API';
    }
    
    $body = wp_remote_retrieve_body($response);
    $data = json_decode($body, true);
    
    if (empty($data['results'])) {
        return 'No se encontraron candidatos';
    }
    
    // Construir HTML para mostrar candidatos
    $output = '<div class="candidatos-grid">';
    
    foreach ($data['results'] as $candidato) {
        $output .= '<div class="candidato-card">';
        if (!empty($candidato['foto_url'])) {
            $output .= '<img src="' . esc_url($candidato['foto_url']) . '" alt="' . esc_attr($candidato['nombre']) . '">';
        }
        $output .= '<h3>' . esc_html($candidato['nombre']) . '</h3>';
        $output .= '<p><strong>Cargo:</strong> ' . esc_html($candidato['cargo']) . '</p>';
        $output .= '<p><strong>Partido:</strong> ' . esc_html($candidato['partido']['nombre']) . ' - Lista ' . esc_html($candidato['partido']['lista']) . '</p>';
        $output .= '<a href="' . esc_url(home_url('/candidato/' . $candidato['id'])) . '" class="button">Ver detalles</a>';
        $output .= '</div>';
    }
    
    $output .= '</div>';
    
    return $output;
}
add_shortcode('candidatos', 'candidatos_shortcode');

// Registrar shortcode para ChatGPT
function chatgpt_shortcode($atts, $content = null) {
    wp_enqueue_script('jquery');
    
    $output = '
    <div class="chatgpt-container">
        <div class="chatgpt-messages" id="chatgpt-messages">
            <div class="message system">Haz una pregunta sobre política ecuatoriana</div>
        </div>
        <div class="chatgpt-input">
            <input type="text" id="chatgpt-question" placeholder="Escribe tu pregunta...">
            <button id="chatgpt-submit">Enviar</button>
        </div>
    </div>
    
    <script>
    jQuery(document).ready(function($) {
        $("#chatgpt-submit").click(function() {
            var question = $("#chatgpt-question").val();
            if (question.trim() === "") return;
            
            // Mostrar pregunta del usuario
            $("#chatgpt-messages").append("<div class=\"message user\">" + question + "</div>");
            $("#chatgpt-question").val("");
            
            // Mostrar indicador de carga
            $("#chatgpt-messages").append("<div class=\"message assistant loading\" id=\"loading-message\">Pensando...</div>");
            
            // Realizar solicitud a la API
            $.ajax({
                url: "https://tu-api-railway.app/api/chatgpt/",
                type: "POST",
                data: JSON.stringify({ pregunta: question }),
                contentType: "application/json",
                success: function(response) {
                    // Eliminar indicador de carga
                    $("#loading-message").remove();
                    
                    // Mostrar respuesta
                    $("#chatgpt-messages").append("<div class=\"message assistant\">" + response.respuesta + "</div>");
                    
                    // Desplazar al final
                    $("#chatgpt-messages").scrollTop($("#chatgpt-messages")[0].scrollHeight);
                },
                error: function() {
                    // Eliminar indicador de carga
                    $("#loading-message").remove();
                    
                    // Mostrar error
                    $("#chatgpt-messages").append("<div class=\"message error\">Error al procesar tu pregunta. Inténtalo de nuevo.</div>");
                }
            });
        });
        
        // Permitir enviar con Enter
        $("#chatgpt-question").keypress(function(e) {
            if (e.which === 13) {
                $("#chatgpt-submit").click();
                return false;
            }
        });
    });
    </script>
    
    <style>
    .chatgpt-container {
        max-width: 600px;
        margin: 0 auto;
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
    }
    .chatgpt-messages {
        height: 300px;
        overflow-y: auto;
        padding: 15px;
        background: #f9f9f9;
    }
    .message {
        margin-bottom: 10px;
        padding: 8px 12px;
        border-radius: 18px;
        max-width: 80%;
        line-height: 1.4;
    }
    .message.system {
        background: #e6e6e6;
        margin: 0 auto 15px;
        text-align: center;
    }
    .message.user {
        background: #dcf8c6;
        margin-left: auto;
    }
    .message.assistant {
        background: #fff;
        border: 1px solid #ddd;
    }
    .message.error {
        background: #ffdddd;
    }
    .chatgpt-input {
        display: flex;
        padding: 10px;
        background: #fff;
    }
    .chatgpt-input input {
        flex: 1;
        padding: 8px 12px;
        border: 1px solid #ddd;
        border-radius: 20px;
        margin-right: 8px;
    }
    .chatgpt-input button {
        background: #0084ff;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 16px;
        cursor: pointer;
    }
    </style>
    ';
    
    return $output;
}
add_shortcode('chatgpt', 'chatgpt_shortcode');