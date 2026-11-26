#
# PySNMP MIB module ERICSSON-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/ERICSSON-TOP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:13 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Gauge32, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, MibIdentifier, Bits, Counter32, Unsigned32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Gauge32", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "MibIdentifier", "Bits", "Counter32", "Unsigned32", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericsson = ModuleIdentity((1, 3, 6, 1, 4, 1, 193))
ericsson.setRevisions(('2008-10-17 00:00', '2002-05-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericsson.setRevisionsDescriptions(('Added email contact address, ericssonModules', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericsson.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericsson.setOrganization('Ericsson AB ')
if mibBuilder.loadTexts: ericsson.setContactInfo('Email: <snmp.mib.contact@ericsson.com>')
if mibBuilder.loadTexts: ericsson.setDescription("This very small module is made available so that\r\n        developers within the Ericsson community can import the\r\n        'ericsson' name into their own MIB modules.  In addition,\r\n        it includes the top-level node for Ericsson Group-wide\r\n        MIB modules.\r\n        \r\n        Document number: 1/196 03-CXC 172 7549, Rev A")
ericssonModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 193, 183))
if mibBuilder.loadTexts: ericssonModules.setStatus('current')
if mibBuilder.loadTexts: ericssonModules.setDescription('ericssonModules provides a root object identifier\r\n        from which MODULE-IDENTITY values may be assigned\r\n        for Ericsson Group-wide MIB modules.')
mibBuilder.exportSymbols("ERICSSON-TOP-MIB", ericssonModules=ericssonModules, ericsson=ericsson, PYSNMP_MODULE_ID=ericsson)
