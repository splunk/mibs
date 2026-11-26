#
# PySNMP MIB module GWTT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gwd/GWTT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:10:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, enterprises, NotificationType, ModuleIdentity, Gauge32, Counter64, MibIdentifier, TimeTicks, Counter32, Bits, IpAddress, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "enterprises", "NotificationType", "ModuleIdentity", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "Bits", "IpAddress", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gwtt = MibIdentifier((1, 3, 6, 1, 4, 1, 10072))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 2))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 3))
snmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 4))
mibBuilder.exportSymbols("GWTT-SMI", chips=chips, cards=cards, devices=devices, snmpProxy=snmpProxy, gwtt=gwtt)
