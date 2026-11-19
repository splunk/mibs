#
# PySNMP MIB module LANOPTICS-ETHERNET-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/LANOPTICS-ETHERNET-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ModuleIdentity, MibIdentifier, enterprises, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ModuleIdentity", "MibIdentifier", "enterprises", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsDot3Monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 3))
etAlertsLevel = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etAlertsLevel.setStatus('mandatory')
etAlertsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etAlertsBuffer.setStatus('mandatory')
etFullStatisticsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etFullStatisticsBuffer.setStatus('mandatory')
etResetBuffers = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etResetBuffers.setStatus('mandatory')
etSlotsTable = MibTable((1, 3, 6, 1, 4, 1, 224, 3, 5), )
if mibBuilder.loadTexts: etSlotsTable.setStatus('mandatory')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1) + (1000, ), Integer32())
etSlotsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 3, 5, 1), ).setIndexNames((0, "LANOPTICS-ETHERNET-OPTION-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: etSlotsEntry.setStatus('mandatory')
etSlotPollStruct = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etSlotPollStruct.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-ETHERNET-OPTION-MIB", etFullStatisticsBuffer=etFullStatisticsBuffer, etResetBuffers=etResetBuffers, lanOpticsDot3Monitor=lanOpticsDot3Monitor, pysmiFakeCol1000=pysmiFakeCol1000, etSlotsEntry=etSlotsEntry, etSlotPollStruct=etSlotPollStruct, etAlertsBuffer=etAlertsBuffer, lanOptics=lanOptics, etAlertsLevel=etAlertsLevel, etSlotsTable=etSlotsTable)
