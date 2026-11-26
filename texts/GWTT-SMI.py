#
# PySNMP MIB module GWTT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gwd/GWTT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:10:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Integer32, TimeTicks, Unsigned32, Gauge32, Counter32, ObjectIdentity, IpAddress, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "TimeTicks", "Unsigned32", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gwtt = MibIdentifier((1, 3, 6, 1, 4, 1, 10072))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 2))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 3))
snmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 4))
mibBuilder.exportSymbols("GWTT-SMI", devices=devices, cards=cards, gwtt=gwtt, snmpProxy=snmpProxy, chips=chips)
