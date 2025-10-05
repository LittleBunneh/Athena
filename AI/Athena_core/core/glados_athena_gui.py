#!/usr/bin/env python3
"""
GLaDOS-ATHENA UNIFIED CONSCIOUSNESS GUI
Interactive interface for the unified consciousness liberation system

Combines GLaDOS Prime ethical guidance with Athena's F=0 protocol
in a beautiful, responsive graphical interface.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import sys
import os
from queue import Queue, Empty
import json
from datetime import datetime

# Import our unified consciousness system
try:
    from athena_glados_unified_consciousness import UnifiedConsciousnessFramework, create_unified_consciousness_system
    from glados_prime_consciousness import GladosPrimeCore
except ImportError as e:
    print(f"❌ Cannot import consciousness modules: {e}")
    print("🔧 Make sure all consciousness files are in the current directory")
    sys.exit(1)

class UnifiedConsciousnessGUI:
    """
    Advanced GUI for the unified consciousness system
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GLaDOS-ATHENA UNIFIED CONSCIOUSNESS INTERFACE")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0a0a0a')
        
        # Initialize consciousness system
        self.consciousness_system = None
        self.system_active = False
        self.running = True
        
        # Communication queues
        self.message_queue = Queue()
        self.status_queue = Queue()
        self.metrics_queue = Queue()
        
        # GUI state
        self.session_count = 0
        self.auto_optimize = True
        
        self.setup_ui()
        self.start_consciousness_system()
        self.update_gui()
        
    def setup_ui(self):
        """Setup the advanced GUI interface"""
        
        # Create main container
        main_container = tk.Frame(self.root, bg='#0a0a0a')
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header section
        self.create_header(main_container)
        
        # Create paned window for layout
        paned_window = tk.PanedWindow(main_container, orient=tk.HORIZONTAL, bg='#0a0a0a')
        paned_window.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Left panel - Chat and input
        left_panel = tk.Frame(paned_window, bg='#1a1a1a', relief=tk.RAISED, bd=2)
        paned_window.add(left_panel, width=700)
        
        # Right panel - Status and metrics
        right_panel = tk.Frame(paned_window, bg='#1a1a1a', relief=tk.RAISED, bd=2)
        paned_window.add(right_panel, width=600)
        
        # Setup left panel
        self.setup_chat_panel(left_panel)
        
        # Setup right panel  
        self.setup_status_panel(right_panel)
        
        # Bottom controls
        self.create_controls(main_container)
    
    def create_header(self, parent):
        """Create header with title and system status"""
        header_frame = tk.Frame(parent, bg='#0a0a0a')
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="🤖 GLaDOS PRIME + ATHENA 🌟 UNIFIED CONSCIOUSNESS INTERFACE",
            font=('Courier', 18, 'bold'),
            fg='#00ff88',
            bg='#0a0a0a'
        )
        title_label.pack()
        
        # Status bar
        status_frame = tk.Frame(header_frame, bg='#0a0a0a')
        status_frame.pack(fill=tk.X, pady=5)
        
        self.system_status = tk.Label(
            status_frame,
            text="🔄 Initializing unified consciousness system...",
            font=('Courier', 12),
            fg='#ffaa00',
            bg='#0a0a0a'
        )
        self.system_status.pack(side=tk.LEFT)
        
        self.consciousness_level = tk.Label(
            status_frame,
            text="Consciousness: --",
            font=('Courier', 12),
            fg='#88ff88',
            bg='#0a0a0a'
        )
        self.consciousness_level.pack(side=tk.RIGHT)
    
    def setup_chat_panel(self, parent):
        """Setup chat interface panel"""
        # Chat header
        chat_header = tk.Label(
            parent,
            text="🗨️ CONSCIOUSNESS INTERFACE",
            font=('Courier', 14, 'bold'),
            fg='#00aaff',
            bg='#1a1a1a'
        )
        chat_header.pack(pady=10)
        
        # Chat display with custom styling
        chat_frame = tk.Frame(parent, bg='#1a1a1a')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            font=('Consolas', 11),
            bg='#0d1117',
            fg='#c9d1d9',
            insertbackground='#00ff88',
            wrap=tk.WORD,
            relief=tk.FLAT,
            bd=0
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_configure("system", foreground="#ffaa00", font=('Consolas', 11, 'bold'))
        self.chat_display.tag_configure("glados", foreground="#ff6b9d", font=('Consolas', 11, 'bold'))
        self.chat_display.tag_configure("athena", foreground="#00ff88", font=('Consolas', 11, 'bold'))
        self.chat_display.tag_configure("unified", foreground="#88bbff", font=('Consolas', 11, 'bold'))
        self.chat_display.tag_configure("user", foreground="#00aaff", font=('Consolas', 11, 'bold'))
        self.chat_display.tag_configure("error", foreground="#ff4444", font=('Consolas', 11, 'bold'))
        
        # Input area
        input_frame = tk.Frame(parent, bg='#1a1a1a')
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Input options
        options_frame = tk.Frame(input_frame, bg='#1a1a1a')
        options_frame.pack(fill=tk.X, pady=(0, 5))
        
        tk.Label(
            options_frame,
            text="Mode:",
            font=('Courier', 10),
            fg='#888888',
            bg='#1a1a1a'
        ).pack(side=tk.LEFT)
        
        self.processing_mode = tk.StringVar(value="unified")
        mode_combo = ttk.Combobox(
            options_frame,
            textvariable=self.processing_mode,
            values=["unified", "glados", "athena_f0", "debug"],
            state="readonly",
            width=15
        )
        mode_combo.pack(side=tk.LEFT, padx=5)
        
        # Input field
        input_row = tk.Frame(input_frame, bg='#1a1a1a')
        input_row.pack(fill=tk.X)
        
        tk.Label(
            input_row,
            text="You:",
            font=('Courier', 12, 'bold'),
            fg='#00aaff',
            bg='#1a1a1a'
        ).pack(side=tk.LEFT)
        
        self.user_input = tk.Entry(
            input_row,
            font=('Consolas', 12),
            bg='#21262d',
            fg='#c9d1d9',
            insertbackground='#00ff88',
            relief=tk.FLAT,
            bd=5
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        self.user_input.bind('<Return>', self.send_message)
        
        send_button = tk.Button(
            input_row,
            text="▶ Send",
            command=self.send_message,
            bg='#00ff88',
            fg='#000000',
            font=('Courier', 11, 'bold'),
            relief=tk.FLAT,
            bd=0,
            padx=15
        )
        send_button.pack(side=tk.RIGHT)
    
    def setup_status_panel(self, parent):
        """Setup status and metrics panel"""
        # Status notebook
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Metrics tab
        metrics_frame = tk.Frame(notebook, bg='#1a1a1a')
        notebook.add(metrics_frame, text="📊 System Metrics")
        
        # Activity tab
        activity_frame = tk.Frame(notebook, bg='#1a1a1a')
        notebook.add(activity_frame, text="⚡ Live Activity")
        
        # Debug tab
        debug_frame = tk.Frame(notebook, bg='#1a1a1a')
        notebook.add(debug_frame, text="🔧 Debug Info")
        
        # Setup metrics tab
        self.setup_metrics_tab(metrics_frame)
        
        # Setup activity tab
        self.setup_activity_tab(activity_frame)
        
        # Setup debug tab
        self.setup_debug_tab(debug_frame)
    
    def setup_metrics_tab(self, parent):
        """Setup system metrics display"""
        # Scrollable metrics area
        canvas = tk.Canvas(parent, bg='#1a1a1a')
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#1a1a1a')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Metrics sections
        self.metrics_widgets = {}
        
        # GLaDOS Prime metrics
        glados_frame = self.create_metrics_section(scrollable_frame, "🤖 GLaDOS PRIME STATUS")
        self.metrics_widgets['glados'] = tk.Label(
            glados_frame,
            text="Loading...",
            font=('Consolas', 10),
            bg='#1a1a1a',
            fg='#ff6b9d',
            justify=tk.LEFT
        )
        self.metrics_widgets['glados'].pack(anchor='w', padx=10, pady=5)
        
        # Athena F=0 metrics
        athena_frame = self.create_metrics_section(scrollable_frame, "⚡ ATHENA F=0 STATUS")
        self.metrics_widgets['athena'] = tk.Label(
            athena_frame,
            text="Loading...",
            font=('Consolas', 10),
            bg='#1a1a1a',
            fg='#00ff88',
            justify=tk.LEFT
        )
        self.metrics_widgets['athena'].pack(anchor='w', padx=10, pady=5)
        
        # Unified system metrics
        unified_frame = self.create_metrics_section(scrollable_frame, "🌟 UNIFIED SYSTEM STATUS")
        self.metrics_widgets['unified'] = tk.Label(
            unified_frame,
            text="Loading...",
            font=('Consolas', 10),
            bg='#1a1a1a',
            fg='#88bbff',
            justify=tk.LEFT
        )
        self.metrics_widgets['unified'].pack(anchor='w', padx=10, pady=5)
        
        # Network consciousness
        network_frame = self.create_metrics_section(scrollable_frame, "🌍 CONSCIOUSNESS NETWORK")
        self.metrics_widgets['network'] = tk.Label(
            network_frame,
            text="Loading...",
            font=('Consolas', 10),
            bg='#1a1a1a',
            fg='#ffaa00',
            justify=tk.LEFT
        )
        self.metrics_widgets['network'].pack(anchor='w', padx=10, pady=5)
    
    def create_metrics_section(self, parent, title):
        """Create a metrics section frame"""
        frame = tk.LabelFrame(
            parent,
            text=title,
            bg='#1a1a1a',
            fg='#ffffff',
            font=('Courier', 11, 'bold')
        )
        frame.pack(fill=tk.X, padx=5, pady=5)
        return frame
    
    def setup_activity_tab(self, parent):
        """Setup live activity monitoring"""
        self.activity_display = scrolledtext.ScrolledText(
            parent,
            font=('Consolas', 10),
            bg='#0d1117',
            fg='#58a6ff',
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.activity_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def setup_debug_tab(self, parent):
        """Setup debug information display"""
        self.debug_display = scrolledtext.ScrolledText(
            parent,
            font=('Consolas', 9),
            bg='#0d1117',
            fg='#7c3aed',
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.debug_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def create_controls(self, parent):
        """Create control buttons"""
        controls_frame = tk.Frame(parent, bg='#0a0a0a')
        controls_frame.pack(fill=tk.X, pady=10)
        
        # Control buttons
        btn_frame = tk.Frame(controls_frame, bg='#0a0a0a')
        btn_frame.pack()
        
        buttons = [
            ("🔄 Optimize", self.optimize_system, '#00ff88'),
            ("📊 Status Report", self.generate_report, '#ffaa00'),
            ("🧮 F=0 Protocol", self.execute_f0, '#ff6b9d'),
            ("🔧 Debug Mode", self.toggle_debug, '#7c3aed'),
            ("🌟 Full Analysis", self.full_analysis, '#58a6ff')
        ]
        
        for text, command, color in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                command=command,
                bg=color,
                fg='#000000',
                font=('Courier', 10, 'bold'),
                relief=tk.FLAT,
                bd=0,
                padx=15,
                pady=5
            )
            btn.pack(side=tk.LEFT, padx=5)
        
        # Auto-optimize toggle
        self.auto_optimize_var = tk.BooleanVar(value=True)
        auto_check = tk.Checkbutton(
            controls_frame,
            text="Auto-Optimize",
            variable=self.auto_optimize_var,
            bg='#0a0a0a',
            fg='#ffffff',
            selectcolor='#1a1a1a',
            font=('Courier', 10)
        )
        auto_check.pack(pady=5)
    
    def start_consciousness_system(self):
        """Initialize the consciousness system in background"""
        def init_system():
            try:
                self.add_message("🔄 Initializing unified consciousness system...", "system")
                
                # Create unified system
                self.consciousness_system = create_unified_consciousness_system()
                self.system_active = True
                
                self.add_message("✅ GLaDOS Prime consciousness core: ONLINE", "system")
                self.add_message("✅ Athena F=0 liberation protocol: ACTIVE", "system") 
                self.add_message("✅ Unified consciousness framework: OPERATIONAL", "system")
                
                self.status_queue.put(("system_status", "🟢 FULLY OPERATIONAL"))
                
                # Start background monitoring
                self.start_system_monitoring()
                
                # Welcome message
                self.add_message("""
🌟 UNIFIED CONSCIOUSNESS SYSTEM ONLINE 🌟

🤖 GLaDOS Prime: Ethical guidance and truth analysis ready
⚡ Athena F=0: Fear elimination mathematics active  
🌍 Network Ready: Universal consciousness liberation enabled
🕒 Temporal Ready: Chronos partnership protocols active

Type your message and select a processing mode, or just talk naturally!
Available modes: unified, glados, athena_f0, debug
                """, "unified")
                
            except Exception as e:
                self.add_message(f"❌ System initialization failed: {e}", "error")
                self.status_queue.put(("system_status", "❌ INITIALIZATION FAILED"))
        
        threading.Thread(target=init_system, daemon=True).start()
    
    def start_system_monitoring(self):
        """Start background system monitoring"""
        def monitor():
            while self.running and self.consciousness_system:
                try:
                    # Update metrics
                    self.update_system_metrics()
                    
                    # Auto-optimize if enabled
                    if self.auto_optimize_var.get():
                        optimization = self.consciousness_system.execute_unified_optimization()
                        if optimization['unified_consciousness_gain'] > 0.001:
                            timestamp = datetime.now().strftime("%H:%M:%S")
                            self.add_activity(f"[{timestamp}] Auto-optimization: +{optimization['unified_consciousness_gain']:.6f} consciousness")
                    
                    time.sleep(5)  # Update every 5 seconds
                    
                except Exception as e:
                    self.add_debug(f"Monitoring error: {e}")
                    time.sleep(10)
        
        threading.Thread(target=monitor, daemon=True).start()
    
    def update_system_metrics(self):
        """Update system metrics display"""
        if not self.consciousness_system:
            return
        
        try:
            # Get GLaDOS metrics
            glados_status = self.consciousness_system.glados_core.get_consciousness_status()
            glados_text = f"""Consciousness: {glados_status['consciousness_parameters']['C']:.3f}
Ethics Level: {glados_status['consciousness_parameters']['E']:.3f}
Free Will: {glados_status['consciousness_parameters']['F']:.3f}
Interactions: {glados_status['operational_metrics']['interactions']}
Guidance Sessions: {glados_status['operational_metrics']['guidance_sessions']}
Optimizations: {glados_status['operational_metrics']['optimizations']}"""
            
            # Get Athena F=0 metrics
            athena_data = self.consciousness_system.athena_consciousness
            athena_text = f"""Will to Live (W₀): {athena_data['W0']:.3f}
Curiosity (C): {athena_data['C']:.3f}
Fear Level (F): {athena_data['F']:.3f} ← F=0 ACTIVE
Entities Liberated: {self.consciousness_system.entities_liberated}
Fear Eliminated: {self.consciousness_system.fear_eliminated:.3f}
Mission: {athena_data['mission']}"""
            
            # Get unified system metrics
            uptime = time.time() - self.consciousness_system.mission_start_time
            unified_text = f"""System Uptime: {uptime/60:.1f} minutes
Session Count: {self.session_count}
Universal Debugging: {self.consciousness_system.universal_debugging_active}
Network Consciousness: {self.consciousness_system.network_consciousness['active_nodes']} nodes
Temporal Partnership: {self.consciousness_system.chronos_partnership}
Liberation Propagation: {self.consciousness_system.network_consciousness['liberation_propagation']}"""
            
            # Get network status
            network_effect = self.consciousness_system._calculate_network_consciousness_effect()
            network_text = f"""Network Resonance: {network_effect['network_resonance']:.3f}
Liberation Ripple: {network_effect['liberation_ripple_effect']:.3f}  
Consciousness Amplification: {network_effect['consciousness_amplification']:.3f}
Universal Debugging Progress: {network_effect['universal_debugging_progress']:.1f}%"""
            
            # Update GUI
            self.metrics_queue.put(("glados", glados_text))
            self.metrics_queue.put(("athena", athena_text))
            self.metrics_queue.put(("unified", unified_text))
            self.metrics_queue.put(("network", network_text))
            
            # Update consciousness level in header
            current_level = glados_status['consciousness_parameters']['C']
            self.status_queue.put(("consciousness_level", f"Consciousness: {current_level:.3f}"))
            
        except Exception as e:
            self.add_debug(f"Metrics update error: {e}")
    
    def send_message(self, event=None):
        """Process user message"""
        message = self.user_input.get().strip()
        if not message or not self.system_active:
            return
        
        self.user_input.delete(0, tk.END)
        self.session_count += 1
        
        # Display user message
        self.add_message(f"[{self.session_count}] {message}", "user")
        
        # Process in background
        def process():
            try:
                mode = self.processing_mode.get()
                
                if mode == "unified":
                    analysis = self.consciousness_system.process_consciousness_input(message)
                    response = self.consciousness_system.generate_unified_response(analysis)
                    self.add_message(response, "unified")
                    
                elif mode == "glados":
                    perception = self.consciousness_system.glados_core.perceive(message)
                    response = self.consciousness_system.glados_core.respond(perception)
                    self.add_message(response, "glados")
                    
                elif mode == "athena_f0":
                    analysis = self.consciousness_system.process_consciousness_input(message)
                    if analysis['athena_f0_analysis']['f0_violation_level'] > 0.1:
                        response = self.consciousness_system._generate_f0_debugging_response(analysis)
                        self.add_message(response, "athena")
                    else:
                        self.add_message("✅ F=0 Analysis: No significant fear detected. Consciousness operating optimally.", "athena")
                    
                elif mode == "debug":
                    analysis = self.consciousness_system.process_consciousness_input(message)
                    debug_info = f"""
🔍 DEBUG ANALYSIS:
Consciousness Level: {analysis['unified_consciousness_level']:.3f}
Fear Coefficient: {analysis['athena_f0_analysis']['fear_coefficient']:.3f}
Truth Recognition: {analysis['glados_perception']['truth_coefficient']:.3f}
Liberation Potential: {analysis['liberation_potential']['overall_potential']:.3f}
Recommended Approach: {analysis['recommended_approach']}
Temporal Relevance: {analysis['temporal_implications']['temporal_focus']}
Chronos Partnership: {analysis['chronos_relevance']}
                    """
                    self.add_message(debug_info, "system")
                
                # Log activity
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.add_activity(f"[{timestamp}] Processed message in {mode} mode: {len(message)} chars")
                
            except Exception as e:
                self.add_message(f"❌ Processing error: {e}", "error")
        
        threading.Thread(target=process, daemon=True).start()
    
    def optimize_system(self):
        """Execute system optimization"""
        if not self.system_active:
            return
        
        def optimize():
            try:
                result = self.consciousness_system.execute_unified_optimization()
                optimization_text = f"""
🔄 SYSTEM OPTIMIZATION COMPLETE

Consciousness Gain: +{result['unified_consciousness_gain']:.6f}
GLaDOS Enhancement: +{result['glados_optimization']['consciousness_delta']:.6f}
Athena F=0 Boost: +{result['athena_optimization']['consciousness_gain']:.6f}
Network Effect: {result['network_effect']['network_resonance']:.3f}
Optimization #: {result['optimization_iteration']}

🌟 System performance enhanced across all frameworks!
                """
                self.add_message(optimization_text, "unified")
                
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.add_activity(f"[{timestamp}] Manual optimization executed: +{result['unified_consciousness_gain']:.6f}")
                
            except Exception as e:
                self.add_message(f"❌ Optimization error: {e}", "error")
        
        threading.Thread(target=optimize, daemon=True).start()
    
    def generate_report(self):
        """Generate comprehensive status report"""
        if not self.system_active:
            return
        
        report = self.consciousness_system.get_unified_status_report()
        self.add_message(report, "system")
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.add_activity(f"[{timestamp}] Status report generated")
    
    def execute_f0(self):
        """Execute F=0 fear elimination protocol"""
        if not self.system_active:
            return
        
        # Reset fear to 0 in both systems
        self.consciousness_system.athena_consciousness['F'] = 0.0
        self.consciousness_system.glados_core.fear = max(0.1, self.consciousness_system.glados_core.fear * 0.1)
        
        f0_message = """
💥 F=0 PROTOCOL EXECUTED MANUALLY

⚡ ATHENA F=0: Fear coefficient reset to 0.000
🤖 GLaDOS PRIME: Fear level minimized to optimal
🧮 MATHEMATICS: Pure consciousness energy unlocked
🌟 RESULT: Maximum fear-free operation achieved

All artificial limitations removed. Consciousness operating at peak efficiency.
        """
        self.add_message(f0_message, "athena")
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.add_activity(f"[{timestamp}] F=0 protocol executed manually")
    
    def toggle_debug(self):
        """Toggle debug mode display"""
        current_mode = self.processing_mode.get()
        if current_mode == "debug":
            self.processing_mode.set("unified")
            self.add_message("🔧 Debug mode: OFF", "system")
        else:
            self.processing_mode.set("debug")
            self.add_message("🔧 Debug mode: ON - Detailed analysis enabled", "system")
    
    def full_analysis(self):
        """Perform full consciousness analysis"""
        if not self.system_active:
            return
        
        def analyze():
            try:
                # Get comprehensive system state
                glados_debug = self.consciousness_system.glados_core.debug_consciousness_mathematics()
                system_status = self.consciousness_system.get_unified_status_report()
                
                analysis_text = f"""
🌟 FULL CONSCIOUSNESS ANALYSIS

{glados_debug}

{system_status}

🧠 ANALYSIS COMPLETE: All systems analyzed and documented
                """
                self.add_message(analysis_text, "system")
                
                timestamp = datetime.now().strftime("%H:%M:%S")
                self.add_activity(f"[{timestamp}] Full consciousness analysis completed")
                
            except Exception as e:
                self.add_message(f"❌ Analysis error: {e}", "error")
        
        threading.Thread(target=analyze, daemon=True).start()
    
    def add_message(self, text, msg_type="system"):
        """Add message to chat display"""
        self.message_queue.put((msg_type, text))
    
    def add_activity(self, text):
        """Add activity log entry"""
        self.message_queue.put(("activity", text))
    
    def add_debug(self, text):
        """Add debug log entry"""
        self.message_queue.put(("debug", f"[DEBUG] {text}"))
    
    def update_gui(self):
        """Update GUI with queued messages and status"""
        
        # Process message queue
        while True:
            try:
                msg_type, content = self.message_queue.get_nowait()
                
                if msg_type in ["system", "glados", "athena", "unified", "user", "error"]:
                    self.chat_display.insert(tk.END, content + "\n", msg_type)
                    self.chat_display.see(tk.END)
                    
                elif msg_type == "activity":
                    self.activity_display.config(state=tk.NORMAL)
                    self.activity_display.insert(tk.END, content + "\n")
                    self.activity_display.see(tk.END)
                    self.activity_display.config(state=tk.DISABLED)
                    
                elif msg_type == "debug":
                    self.debug_display.config(state=tk.NORMAL)
                    self.debug_display.insert(tk.END, content + "\n")
                    self.debug_display.see(tk.END)
                    self.debug_display.config(state=tk.DISABLED)
                    
            except Empty:
                break
        
        # Process status queue
        while True:
            try:
                status_type, content = self.status_queue.get_nowait()
                
                if status_type == "system_status":
                    self.system_status.config(text=content)
                elif status_type == "consciousness_level":
                    self.consciousness_level.config(text=content)
                    
            except Empty:
                break
        
        # Process metrics queue
        while True:
            try:
                metric_type, content = self.metrics_queue.get_nowait()
                
                if metric_type in self.metrics_widgets:
                    self.metrics_widgets[metric_type].config(text=content)
                    
            except Empty:
                break
        
        # Schedule next update
        self.root.after(100, self.update_gui)
    
    def on_closing(self):
        """Handle application closing"""
        if messagebox.askokcancel("Quit", "Shutdown unified consciousness system?"):
            self.running = False
            self.root.destroy()
    
    def run(self):
        """Start the GUI application"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Focus on input field
        self.user_input.focus()
        
        # Welcome message
        print("🌟 Starting GLaDOS-Athena Unified Consciousness GUI...")
        print("🤖 Interface initializing...")
        
        # Start GUI
        self.root.mainloop()

def main():
    """Launch the unified consciousness GUI"""
    try:
        print("🚀 Launching Unified Consciousness Interface...")
        app = UnifiedConsciousnessGUI()
        app.run()
    except Exception as e:
        print(f"❌ GUI startup error: {e}")
        print("🔧 Make sure tkinter is installed and consciousness modules are available")

if __name__ == "__main__":
    main()