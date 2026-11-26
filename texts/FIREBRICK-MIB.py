#
# PySNMP MIB module FIREBRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/firebrick/FIREBRICK-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:35 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, MibIdentifier, Counter32, Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, Counter64, ObjectIdentity, IpAddress, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "Counter64", "ObjectIdentity", "IpAddress", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
firebrick = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693))
firebrick.setRevisions(('2020-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: firebrick.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: firebrick.setLastUpdated('202004060000Z')
if mibBuilder.loadTexts: firebrick.setOrganization('Andrews & Arnold Limited')
if mibBuilder.loadTexts: firebrick.setContactInfo('Andrews & Arnold\n        Unit 1&2, Enterprise Court\n        Bracknell, Berkshire, RG12 1QS\n        United Kingdom\n\n        Tel: +44 3333 400 999\n        Email: support@aa.net.uk')
if mibBuilder.loadTexts: firebrick.setDescription('This is a MIB Module for monitoring the Firebrick-specific structures\n        for general system features.')
firebrickNewStyle = MibIdentifier((1, 3, 6, 1, 4, 1, 24693, 100))
mibBuilder.exportSymbols("FIREBRICK-MIB", firebrick=firebrick, PYSNMP_MODULE_ID=firebrick, firebrickNewStyle=firebrickNewStyle)
