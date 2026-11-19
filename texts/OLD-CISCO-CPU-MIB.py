#
# PySNMP MIB module OLD-CISCO-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/OLD-CISCO-CPU-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lcpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 1))
busyPer = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyPer.setStatus('mandatory')
if mibBuilder.loadTexts: busyPer.setDescription('CPU busy percentage in the last 5 second\n                           period. Not the last 5 realtime seconds but\n                           the last 5 second period in the scheduler.')
avgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy1.setStatus('mandatory')
if mibBuilder.loadTexts: avgBusy1.setDescription('1 minute exponentially-decayed moving\n                           average of the CPU busy percentage.')
avgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy5.setStatus('mandatory')
if mibBuilder.loadTexts: avgBusy5.setDescription('5 minute exponentially-decayed moving\n                           average of the CPU busy percentage.')
idleCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleCount.setStatus('mandatory')
if mibBuilder.loadTexts: idleCount.setDescription('cisco internal variable. not to be used')
idleWired = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleWired.setStatus('mandatory')
if mibBuilder.loadTexts: idleWired.setDescription('cisco internal variable. not to be used')
mibBuilder.exportSymbols("OLD-CISCO-CPU-MIB", idleCount=idleCount, idleWired=idleWired, busyPer=busyPer, avgBusy5=avgBusy5, lcpu=lcpu, avgBusy1=avgBusy1)
