# Generated from .\typescript.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .typescriptParser import typescriptParser
else:
    from typescriptParser import typescriptParser

# This class defines a complete listener for a parse tree produced by typescriptParser.
class typescriptListener(ParseTreeListener):

    # Enter a parse tree produced by typescriptParser#sAll.
    def enterSAll(self, ctx:typescriptParser.SAllContext):
        pass

    # Exit a parse tree produced by typescriptParser#sAll.
    def exitSAll(self, ctx:typescriptParser.SAllContext):
        pass


    # Enter a parse tree produced by typescriptParser#sOperand.
    def enterSOperand(self, ctx:typescriptParser.SOperandContext):
        pass

    # Exit a parse tree produced by typescriptParser#sOperand.
    def exitSOperand(self, ctx:typescriptParser.SOperandContext):
        pass


    # Enter a parse tree produced by typescriptParser#sOperator.
    def enterSOperator(self, ctx:typescriptParser.SOperatorContext):
        pass

    # Exit a parse tree produced by typescriptParser#sOperator.
    def exitSOperator(self, ctx:typescriptParser.SOperatorContext):
        pass


    # Enter a parse tree produced by typescriptParser#sExpression.
    def enterSExpression(self, ctx:typescriptParser.SExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sExpression.
    def exitSExpression(self, ctx:typescriptParser.SExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sTerm.
    def enterSTerm(self, ctx:typescriptParser.STermContext):
        pass

    # Exit a parse tree produced by typescriptParser#sTerm.
    def exitSTerm(self, ctx:typescriptParser.STermContext):
        pass


    # Enter a parse tree produced by typescriptParser#sValue.
    def enterSValue(self, ctx:typescriptParser.SValueContext):
        pass

    # Exit a parse tree produced by typescriptParser#sValue.
    def exitSValue(self, ctx:typescriptParser.SValueContext):
        pass


    # Enter a parse tree produced by typescriptParser#sInvocation.
    def enterSInvocation(self, ctx:typescriptParser.SInvocationContext):
        pass

    # Exit a parse tree produced by typescriptParser#sInvocation.
    def exitSInvocation(self, ctx:typescriptParser.SInvocationContext):
        pass


    # Enter a parse tree produced by typescriptParser#sControl.
    def enterSControl(self, ctx:typescriptParser.SControlContext):
        pass

    # Exit a parse tree produced by typescriptParser#sControl.
    def exitSControl(self, ctx:typescriptParser.SControlContext):
        pass


    # Enter a parse tree produced by typescriptParser#sStatement.
    def enterSStatement(self, ctx:typescriptParser.SStatementContext):
        pass

    # Exit a parse tree produced by typescriptParser#sStatement.
    def exitSStatement(self, ctx:typescriptParser.SStatementContext):
        pass


    # Enter a parse tree produced by typescriptParser#sPlus.
    def enterSPlus(self, ctx:typescriptParser.SPlusContext):
        pass

    # Exit a parse tree produced by typescriptParser#sPlus.
    def exitSPlus(self, ctx:typescriptParser.SPlusContext):
        pass


    # Enter a parse tree produced by typescriptParser#sMinus.
    def enterSMinus(self, ctx:typescriptParser.SMinusContext):
        pass

    # Exit a parse tree produced by typescriptParser#sMinus.
    def exitSMinus(self, ctx:typescriptParser.SMinusContext):
        pass


    # Enter a parse tree produced by typescriptParser#sMul.
    def enterSMul(self, ctx:typescriptParser.SMulContext):
        pass

    # Exit a parse tree produced by typescriptParser#sMul.
    def exitSMul(self, ctx:typescriptParser.SMulContext):
        pass


    # Enter a parse tree produced by typescriptParser#sDiv.
    def enterSDiv(self, ctx:typescriptParser.SDivContext):
        pass

    # Exit a parse tree produced by typescriptParser#sDiv.
    def exitSDiv(self, ctx:typescriptParser.SDivContext):
        pass


    # Enter a parse tree produced by typescriptParser#sPower.
    def enterSPower(self, ctx:typescriptParser.SPowerContext):
        pass

    # Exit a parse tree produced by typescriptParser#sPower.
    def exitSPower(self, ctx:typescriptParser.SPowerContext):
        pass


    # Enter a parse tree produced by typescriptParser#sAnd.
    def enterSAnd(self, ctx:typescriptParser.SAndContext):
        pass

    # Exit a parse tree produced by typescriptParser#sAnd.
    def exitSAnd(self, ctx:typescriptParser.SAndContext):
        pass


    # Enter a parse tree produced by typescriptParser#sOr.
    def enterSOr(self, ctx:typescriptParser.SOrContext):
        pass

    # Exit a parse tree produced by typescriptParser#sOr.
    def exitSOr(self, ctx:typescriptParser.SOrContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNot.
    def enterSNot(self, ctx:typescriptParser.SNotContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNot.
    def exitSNot(self, ctx:typescriptParser.SNotContext):
        pass


    # Enter a parse tree produced by typescriptParser#sEquals.
    def enterSEquals(self, ctx:typescriptParser.SEqualsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sEquals.
    def exitSEquals(self, ctx:typescriptParser.SEqualsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNotEquals.
    def enterSNotEquals(self, ctx:typescriptParser.SNotEqualsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNotEquals.
    def exitSNotEquals(self, ctx:typescriptParser.SNotEqualsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sLowerThan.
    def enterSLowerThan(self, ctx:typescriptParser.SLowerThanContext):
        pass

    # Exit a parse tree produced by typescriptParser#sLowerThan.
    def exitSLowerThan(self, ctx:typescriptParser.SLowerThanContext):
        pass


    # Enter a parse tree produced by typescriptParser#sLowerEquals.
    def enterSLowerEquals(self, ctx:typescriptParser.SLowerEqualsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sLowerEquals.
    def exitSLowerEquals(self, ctx:typescriptParser.SLowerEqualsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sGreaterThan.
    def enterSGreaterThan(self, ctx:typescriptParser.SGreaterThanContext):
        pass

    # Exit a parse tree produced by typescriptParser#sGreaterThan.
    def exitSGreaterThan(self, ctx:typescriptParser.SGreaterThanContext):
        pass


    # Enter a parse tree produced by typescriptParser#sGreaterEquals.
    def enterSGreaterEquals(self, ctx:typescriptParser.SGreaterEqualsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sGreaterEquals.
    def exitSGreaterEquals(self, ctx:typescriptParser.SGreaterEqualsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sArithmeticExpression.
    def enterSArithmeticExpression(self, ctx:typescriptParser.SArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sArithmeticExpression.
    def exitSArithmeticExpression(self, ctx:typescriptParser.SArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sArithmeticTerm.
    def enterSArithmeticTerm(self, ctx:typescriptParser.SArithmeticTermContext):
        pass

    # Exit a parse tree produced by typescriptParser#sArithmeticTerm.
    def exitSArithmeticTerm(self, ctx:typescriptParser.SArithmeticTermContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBooleanOperand.
    def enterSBooleanOperand(self, ctx:typescriptParser.SBooleanOperandContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBooleanOperand.
    def exitSBooleanOperand(self, ctx:typescriptParser.SBooleanOperandContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBooleanOperator.
    def enterSBooleanOperator(self, ctx:typescriptParser.SBooleanOperatorContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBooleanOperator.
    def exitSBooleanOperator(self, ctx:typescriptParser.SBooleanOperatorContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBooleanExpression.
    def enterSBooleanExpression(self, ctx:typescriptParser.SBooleanExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBooleanExpression.
    def exitSBooleanExpression(self, ctx:typescriptParser.SBooleanExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBooleanTerm.
    def enterSBooleanTerm(self, ctx:typescriptParser.SBooleanTermContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBooleanTerm.
    def exitSBooleanTerm(self, ctx:typescriptParser.SBooleanTermContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNumberOperand.
    def enterSNumberOperand(self, ctx:typescriptParser.SNumberOperandContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNumberOperand.
    def exitSNumberOperand(self, ctx:typescriptParser.SNumberOperandContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNumberOperator.
    def enterSNumberOperator(self, ctx:typescriptParser.SNumberOperatorContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNumberOperator.
    def exitSNumberOperator(self, ctx:typescriptParser.SNumberOperatorContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNumberExpression.
    def enterSNumberExpression(self, ctx:typescriptParser.SNumberExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNumberExpression.
    def exitSNumberExpression(self, ctx:typescriptParser.SNumberExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNumberTerm.
    def enterSNumberTerm(self, ctx:typescriptParser.SNumberTermContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNumberTerm.
    def exitSNumberTerm(self, ctx:typescriptParser.SNumberTermContext):
        pass


    # Enter a parse tree produced by typescriptParser#sStringOperand.
    def enterSStringOperand(self, ctx:typescriptParser.SStringOperandContext):
        pass

    # Exit a parse tree produced by typescriptParser#sStringOperand.
    def exitSStringOperand(self, ctx:typescriptParser.SStringOperandContext):
        pass


    # Enter a parse tree produced by typescriptParser#sStringOperator.
    def enterSStringOperator(self, ctx:typescriptParser.SStringOperatorContext):
        pass

    # Exit a parse tree produced by typescriptParser#sStringOperator.
    def exitSStringOperator(self, ctx:typescriptParser.SStringOperatorContext):
        pass


    # Enter a parse tree produced by typescriptParser#sStringExpression.
    def enterSStringExpression(self, ctx:typescriptParser.SStringExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sStringExpression.
    def exitSStringExpression(self, ctx:typescriptParser.SStringExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sStringTerm.
    def enterSStringTerm(self, ctx:typescriptParser.SStringTermContext):
        pass

    # Exit a parse tree produced by typescriptParser#sStringTerm.
    def exitSStringTerm(self, ctx:typescriptParser.SStringTermContext):
        pass


    # Enter a parse tree produced by typescriptParser#sConcatOperand.
    def enterSConcatOperand(self, ctx:typescriptParser.SConcatOperandContext):
        pass

    # Exit a parse tree produced by typescriptParser#sConcatOperand.
    def exitSConcatOperand(self, ctx:typescriptParser.SConcatOperandContext):
        pass


    # Enter a parse tree produced by typescriptParser#sConcatExpression.
    def enterSConcatExpression(self, ctx:typescriptParser.SConcatExpressionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sConcatExpression.
    def exitSConcatExpression(self, ctx:typescriptParser.SConcatExpressionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sConcatLeft.
    def enterSConcatLeft(self, ctx:typescriptParser.SConcatLeftContext):
        pass

    # Exit a parse tree produced by typescriptParser#sConcatLeft.
    def exitSConcatLeft(self, ctx:typescriptParser.SConcatLeftContext):
        pass


    # Enter a parse tree produced by typescriptParser#sConcatRight.
    def enterSConcatRight(self, ctx:typescriptParser.SConcatRightContext):
        pass

    # Exit a parse tree produced by typescriptParser#sConcatRight.
    def exitSConcatRight(self, ctx:typescriptParser.SConcatRightContext):
        pass


    # Enter a parse tree produced by typescriptParser#sConcatBoth.
    def enterSConcatBoth(self, ctx:typescriptParser.SConcatBothContext):
        pass

    # Exit a parse tree produced by typescriptParser#sConcatBoth.
    def exitSConcatBoth(self, ctx:typescriptParser.SConcatBothContext):
        pass


    # Enter a parse tree produced by typescriptParser#sType.
    def enterSType(self, ctx:typescriptParser.STypeContext):
        pass

    # Exit a parse tree produced by typescriptParser#sType.
    def exitSType(self, ctx:typescriptParser.STypeContext):
        pass


    # Enter a parse tree produced by typescriptParser#sOptional.
    def enterSOptional(self, ctx:typescriptParser.SOptionalContext):
        pass

    # Exit a parse tree produced by typescriptParser#sOptional.
    def exitSOptional(self, ctx:typescriptParser.SOptionalContext):
        pass


    # Enter a parse tree produced by typescriptParser#sPropertyDelete.
    def enterSPropertyDelete(self, ctx:typescriptParser.SPropertyDeleteContext):
        pass

    # Exit a parse tree produced by typescriptParser#sPropertyDelete.
    def exitSPropertyDelete(self, ctx:typescriptParser.SPropertyDeleteContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunction.
    def enterSFunction(self, ctx:typescriptParser.SFunctionContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunction.
    def exitSFunction(self, ctx:typescriptParser.SFunctionContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionArg.
    def enterSFunctionArg(self, ctx:typescriptParser.SFunctionArgContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionArg.
    def exitSFunctionArg(self, ctx:typescriptParser.SFunctionArgContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionArgs.
    def enterSFunctionArgs(self, ctx:typescriptParser.SFunctionArgsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionArgs.
    def exitSFunctionArgs(self, ctx:typescriptParser.SFunctionArgsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionArgDef.
    def enterSFunctionArgDef(self, ctx:typescriptParser.SFunctionArgDefContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionArgDef.
    def exitSFunctionArgDef(self, ctx:typescriptParser.SFunctionArgDefContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionArgDefs.
    def enterSFunctionArgDefs(self, ctx:typescriptParser.SFunctionArgDefsContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionArgDefs.
    def exitSFunctionArgDefs(self, ctx:typescriptParser.SFunctionArgDefsContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionHead.
    def enterSFunctionHead(self, ctx:typescriptParser.SFunctionHeadContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionHead.
    def exitSFunctionHead(self, ctx:typescriptParser.SFunctionHeadContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionTail.
    def enterSFunctionTail(self, ctx:typescriptParser.SFunctionTailContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionTail.
    def exitSFunctionTail(self, ctx:typescriptParser.SFunctionTailContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionCall.
    def enterSFunctionCall(self, ctx:typescriptParser.SFunctionCallContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionCall.
    def exitSFunctionCall(self, ctx:typescriptParser.SFunctionCallContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionLambda.
    def enterSFunctionLambda(self, ctx:typescriptParser.SFunctionLambdaContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionLambda.
    def exitSFunctionLambda(self, ctx:typescriptParser.SFunctionLambdaContext):
        pass


    # Enter a parse tree produced by typescriptParser#sProperty.
    def enterSProperty(self, ctx:typescriptParser.SPropertyContext):
        pass

    # Exit a parse tree produced by typescriptParser#sProperty.
    def exitSProperty(self, ctx:typescriptParser.SPropertyContext):
        pass


    # Enter a parse tree produced by typescriptParser#sPropertyAware.
    def enterSPropertyAware(self, ctx:typescriptParser.SPropertyAwareContext):
        pass

    # Exit a parse tree produced by typescriptParser#sPropertyAware.
    def exitSPropertyAware(self, ctx:typescriptParser.SPropertyAwareContext):
        pass


    # Enter a parse tree produced by typescriptParser#sPropertyAccess.
    def enterSPropertyAccess(self, ctx:typescriptParser.SPropertyAccessContext):
        pass

    # Exit a parse tree produced by typescriptParser#sPropertyAccess.
    def exitSPropertyAccess(self, ctx:typescriptParser.SPropertyAccessContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionAware.
    def enterSFunctionAware(self, ctx:typescriptParser.SFunctionAwareContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionAware.
    def exitSFunctionAware(self, ctx:typescriptParser.SFunctionAwareContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFunctionAccess.
    def enterSFunctionAccess(self, ctx:typescriptParser.SFunctionAccessContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFunctionAccess.
    def exitSFunctionAccess(self, ctx:typescriptParser.SFunctionAccessContext):
        pass


    # Enter a parse tree produced by typescriptParser#sLine.
    def enterSLine(self, ctx:typescriptParser.SLineContext):
        pass

    # Exit a parse tree produced by typescriptParser#sLine.
    def exitSLine(self, ctx:typescriptParser.SLineContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBody.
    def enterSBody(self, ctx:typescriptParser.SBodyContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBody.
    def exitSBody(self, ctx:typescriptParser.SBodyContext):
        pass


    # Enter a parse tree produced by typescriptParser#sReturn.
    def enterSReturn(self, ctx:typescriptParser.SReturnContext):
        pass

    # Exit a parse tree produced by typescriptParser#sReturn.
    def exitSReturn(self, ctx:typescriptParser.SReturnContext):
        pass


    # Enter a parse tree produced by typescriptParser#sIf.
    def enterSIf(self, ctx:typescriptParser.SIfContext):
        pass

    # Exit a parse tree produced by typescriptParser#sIf.
    def exitSIf(self, ctx:typescriptParser.SIfContext):
        pass


    # Enter a parse tree produced by typescriptParser#sElse.
    def enterSElse(self, ctx:typescriptParser.SElseContext):
        pass

    # Exit a parse tree produced by typescriptParser#sElse.
    def exitSElse(self, ctx:typescriptParser.SElseContext):
        pass


    # Enter a parse tree produced by typescriptParser#sElseIf.
    def enterSElseIf(self, ctx:typescriptParser.SElseIfContext):
        pass

    # Exit a parse tree produced by typescriptParser#sElseIf.
    def exitSElseIf(self, ctx:typescriptParser.SElseIfContext):
        pass


    # Enter a parse tree produced by typescriptParser#sString.
    def enterSString(self, ctx:typescriptParser.SStringContext):
        pass

    # Exit a parse tree produced by typescriptParser#sString.
    def exitSString(self, ctx:typescriptParser.SStringContext):
        pass


    # Enter a parse tree produced by typescriptParser#sNumber.
    def enterSNumber(self, ctx:typescriptParser.SNumberContext):
        pass

    # Exit a parse tree produced by typescriptParser#sNumber.
    def exitSNumber(self, ctx:typescriptParser.SNumberContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBoolean.
    def enterSBoolean(self, ctx:typescriptParser.SBooleanContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBoolean.
    def exitSBoolean(self, ctx:typescriptParser.SBooleanContext):
        pass


    # Enter a parse tree produced by typescriptParser#sArray.
    def enterSArray(self, ctx:typescriptParser.SArrayContext):
        pass

    # Exit a parse tree produced by typescriptParser#sArray.
    def exitSArray(self, ctx:typescriptParser.SArrayContext):
        pass


    # Enter a parse tree produced by typescriptParser#sMap.
    def enterSMap(self, ctx:typescriptParser.SMapContext):
        pass

    # Exit a parse tree produced by typescriptParser#sMap.
    def exitSMap(self, ctx:typescriptParser.SMapContext):
        pass


    # Enter a parse tree produced by typescriptParser#sEndlessLoop.
    def enterSEndlessLoop(self, ctx:typescriptParser.SEndlessLoopContext):
        pass

    # Exit a parse tree produced by typescriptParser#sEndlessLoop.
    def exitSEndlessLoop(self, ctx:typescriptParser.SEndlessLoopContext):
        pass


    # Enter a parse tree produced by typescriptParser#sWhile.
    def enterSWhile(self, ctx:typescriptParser.SWhileContext):
        pass

    # Exit a parse tree produced by typescriptParser#sWhile.
    def exitSWhile(self, ctx:typescriptParser.SWhileContext):
        pass


    # Enter a parse tree produced by typescriptParser#sDoWhile.
    def enterSDoWhile(self, ctx:typescriptParser.SDoWhileContext):
        pass

    # Exit a parse tree produced by typescriptParser#sDoWhile.
    def exitSDoWhile(self, ctx:typescriptParser.SDoWhileContext):
        pass


    # Enter a parse tree produced by typescriptParser#sFor.
    def enterSFor(self, ctx:typescriptParser.SForContext):
        pass

    # Exit a parse tree produced by typescriptParser#sFor.
    def exitSFor(self, ctx:typescriptParser.SForContext):
        pass


    # Enter a parse tree produced by typescriptParser#sForOf.
    def enterSForOf(self, ctx:typescriptParser.SForOfContext):
        pass

    # Exit a parse tree produced by typescriptParser#sForOf.
    def exitSForOf(self, ctx:typescriptParser.SForOfContext):
        pass


    # Enter a parse tree produced by typescriptParser#sForIn.
    def enterSForIn(self, ctx:typescriptParser.SForInContext):
        pass

    # Exit a parse tree produced by typescriptParser#sForIn.
    def exitSForIn(self, ctx:typescriptParser.SForInContext):
        pass


    # Enter a parse tree produced by typescriptParser#sLoopTail.
    def enterSLoopTail(self, ctx:typescriptParser.SLoopTailContext):
        pass

    # Exit a parse tree produced by typescriptParser#sLoopTail.
    def exitSLoopTail(self, ctx:typescriptParser.SLoopTailContext):
        pass


    # Enter a parse tree produced by typescriptParser#sContinue.
    def enterSContinue(self, ctx:typescriptParser.SContinueContext):
        pass

    # Exit a parse tree produced by typescriptParser#sContinue.
    def exitSContinue(self, ctx:typescriptParser.SContinueContext):
        pass


    # Enter a parse tree produced by typescriptParser#sBreak.
    def enterSBreak(self, ctx:typescriptParser.SBreakContext):
        pass

    # Exit a parse tree produced by typescriptParser#sBreak.
    def exitSBreak(self, ctx:typescriptParser.SBreakContext):
        pass


    # Enter a parse tree produced by typescriptParser#sMutableVar.
    def enterSMutableVar(self, ctx:typescriptParser.SMutableVarContext):
        pass

    # Exit a parse tree produced by typescriptParser#sMutableVar.
    def exitSMutableVar(self, ctx:typescriptParser.SMutableVarContext):
        pass


    # Enter a parse tree produced by typescriptParser#sImmutableVar.
    def enterSImmutableVar(self, ctx:typescriptParser.SImmutableVarContext):
        pass

    # Exit a parse tree produced by typescriptParser#sImmutableVar.
    def exitSImmutableVar(self, ctx:typescriptParser.SImmutableVarContext):
        pass


    # Enter a parse tree produced by typescriptParser#sAssignment.
    def enterSAssignment(self, ctx:typescriptParser.SAssignmentContext):
        pass

    # Exit a parse tree produced by typescriptParser#sAssignment.
    def exitSAssignment(self, ctx:typescriptParser.SAssignmentContext):
        pass


    # Enter a parse tree produced by typescriptParser#sIncrement.
    def enterSIncrement(self, ctx:typescriptParser.SIncrementContext):
        pass

    # Exit a parse tree produced by typescriptParser#sIncrement.
    def exitSIncrement(self, ctx:typescriptParser.SIncrementContext):
        pass


    # Enter a parse tree produced by typescriptParser#sDecrement.
    def enterSDecrement(self, ctx:typescriptParser.SDecrementContext):
        pass

    # Exit a parse tree produced by typescriptParser#sDecrement.
    def exitSDecrement(self, ctx:typescriptParser.SDecrementContext):
        pass



del typescriptParser