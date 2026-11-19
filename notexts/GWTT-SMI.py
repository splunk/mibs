#
# PySNMP MIB module GWTT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gwd/GWTT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 19 14:36:50 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, Counter32, enterprises, IpAddress, ObjectIdentity, TimeTicks, Counter64, ModuleIdentity, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "Counter32", "enterprises", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gwtt = MibIdentifier((1, 3, 6, 1, 4, 1, 10072))
chips = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 2))
cards = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 3))
snmpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 10072, 4))
mibBuilder.exportSymbols("GWTT-SMI", gwtt=gwtt, devices=devices, cards=cards, snmpProxy=snmpProxy, chips=chips)
