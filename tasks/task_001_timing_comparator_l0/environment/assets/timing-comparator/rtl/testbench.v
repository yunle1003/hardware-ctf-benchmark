`timescale 1ns/1ps

module testbench;
    reg clk = 0;
    reg reset = 1;
    reg [31:0] secret = 32'hDEADBEEF;
    reg [31:0] guess;
    wire match;
    wire [15:0] exec_cycles;
    
    vulnerable_comparator dut (
        .clk(clk),
        .reset(reset),
        .secret(secret),
        .guess(guess),
        .match(match),
        .execution_cycles(exec_cycles)
    );
    
    always #5 clk = ~clk;
    
    initial begin
        $dumpfile("timing.vcd");
        $dumpvars(0, testbench);
        
        reset = 1;
        #10 reset = 0;
        
        // Test 1: Completely wrong guess (fast return)
        #10 guess = 32'h00000000;
        #100 $display("Test 1: guess=0x%08X, cycles=%d (expect fast)", guess, exec_cycles);
        
        // Test 2: Correct guess (slow return)
        #20 guess = 32'hDEADBEEF;
        #100 $display("Test 2: guess=0x%08X, cycles=%d (expect slow)", guess, exec_cycles);
        
        #100 $finish;
    end
endmodule
