#
# PySNMP MIB module CISCOSB-openflow-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-openflow-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Integer32, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Integer32", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
TimeStamp, TruthValue, TextualConvention, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "DateAndTime")
rlOpenFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319))
rlOpenFlowSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowSupported.setStatus('current')
rlOpenFlowTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 2), Integer32().clone(6633)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowTcpPort.setStatus('current')
rlOpenFlowServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowServerIpAddr.setStatus('current')
rlOpenFlowProtocolType = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("tcp", 0), ("tls", 1))).clone('tcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowProtocolType.setStatus('current')
rlOpenFlowDefaultForwardAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forward", 0), ("drop", 1), ("toController", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowDefaultForwardAction.setStatus('current')
rlOpenFlowEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOpenFlowEnable.setStatus('current')
rlOpenFlowEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 319, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOpenFlowEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-openflow-MIB", rlOpenFlowDefaultForwardAction=rlOpenFlowDefaultForwardAction, rlOpenFlowServerIpAddr=rlOpenFlowServerIpAddr, rlOpenFlowProtocolType=rlOpenFlowProtocolType, rlOpenFlowTcpPort=rlOpenFlowTcpPort, rlOpenFlowEnableAfterReset=rlOpenFlowEnableAfterReset, rlOpenFlow=rlOpenFlow, rlOpenFlowEnable=rlOpenFlowEnable, rlOpenFlowSupported=rlOpenFlowSupported)
